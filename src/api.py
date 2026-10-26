"""Local, read-only API for the static officer interface.

It exposes only label-free views through ``src.db.connect(readonly=True)``.
The follow-up endpoint compiles one of three fixed SELECT templates; no caller
can provide SQL. This server is intentionally local-only.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import time
from collections import defaultdict, deque
from decimal import Decimal
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.parse import parse_qs, urlparse

from src.case_notes import build_case_note, validate_note
from src.db import connect
from src.followup import execute_followup, plan_question

ROOT = Path(__file__).resolve().parents[1]
MAX_ROWS = 200
TIMEOUT_SECONDS = 30
RATE_LIMIT = 60
RATE_WINDOW_SECONDS = 60
FACTORY_ID = re.compile(r"F\d{6}")
ACTIVITY: deque[dict] = deque(maxlen=100)
REQUESTS: dict[str, deque[float]] = defaultdict(deque)
LOCK = Lock()


def git_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def serialise(value):
    if isinstance(value, Decimal):
        return float(value)
    raise TypeError(f"Unsupported JSON value: {type(value).__name__}")


def query(sql: str) -> list[dict]:
    connection = connect(readonly=True)
    try:
        statement = connection.execute(sql)
        values = statement.fetchall()
        if len(values) > MAX_ROWS:
            raise ValueError("Row limit exceeded.")
        columns = [column.lower() for column in statement.column_names()]
        return [dict(zip(columns, row)) for row in values]
    finally:
        connection.close()


def require_factory(value: str) -> str:
    if not FACTORY_ID.fullmatch(value):
        raise ValueError("Factory ID must have form F followed by six digits.")
    return value


def queue(params: dict[str, list[str]]) -> dict:
    view = params.get("view", ["monthly"])[0]
    if view not in {"monthly", "factory", "disposition"}:
        raise ValueError("view must be monthly, factory or disposition")
    if view == "disposition":
        disposition = params.get("disposition", ["cleared"])[0]
        prefix = "Cleared:%" if disposition == "cleared" else "Review-only:%" if disposition == "review" else None
        if prefix is None:
            raise ValueError("disposition must be cleared or review")
        return {"view": view, "rows": query("""
          SELECT FACTORY_ID, PERIOD_MONTH, SOURCE_FAMILY, DISPOSITION
          FROM GST_EVIDENCE.V_SINGLE_SIGNAL_DISPOSITIONS
          WHERE SIGNAL_COUNT=1 AND DISPOSITION LIKE '%s'
          ORDER BY PERIOD_MONTH, FACTORY_ID LIMIT 200
        """ % prefix)}
    if view == "monthly":
        return {"view": view, "k": 3, "rows": query("""
          SELECT FACTORY_ID, PERIOD_MONTH, SIGNAL_COUNT, WEAKEST_LINK_NORMALISED_GAP,
                 ESTIMATED_TAX_EXPOSURE_INR, STATUS
          FROM GST_EVIDENCE.V_RANKED_CASES WHERE STATUS='prioritise'
          ORDER BY SIGNAL_COUNT DESC, WEAKEST_LINK_NORMALISED_GAP DESC,
                   ESTIMATED_TAX_EXPOSURE_INR DESC, FACTORY_ID LIMIT 200
        """)}
    return {"view": view, "k": 3, "rows": query("""
      SELECT FACTORY_ID, COUNT(*) PRIORITISED_MONTHS, MAX(SIGNAL_COUNT) MAX_SIGNAL_COUNT,
             MIN(WEAKEST_LINK_NORMALISED_GAP) WEAKEST_LINK_NORMALISED_GAP,
             SUM(ESTIMATED_TAX_EXPOSURE_INR) ESTIMATED_TAX_EXPOSURE_INR
      FROM GST_EVIDENCE.V_RANKED_CASES WHERE STATUS='prioritise'
      GROUP BY FACTORY_ID HAVING COUNT(*)>=3
      ORDER BY MAX(SIGNAL_COUNT) DESC, MIN(WEAKEST_LINK_NORMALISED_GAP) DESC,
               SUM(ESTIMATED_TAX_EXPOSURE_INR) DESC, FACTORY_ID LIMIT 200
    """)}


def case(factory_id: str) -> dict:
    factory_id = require_factory(factory_id)
    timeline = query("SELECT PERIOD_MONTH,SIGNAL_COUNT,TOTAL_SEVERITY,WEAKEST_LINK_NORMALISED_GAP,"
                     "ESTIMATED_TAX_EXPOSURE_INR,STATUS FROM GST_EVIDENCE.V_RANKED_CASES "
                     f"WHERE FACTORY_ID='{factory_id}' ORDER BY PERIOD_MONTH LIMIT 12")
    evidence = query("SELECT FACTORY_ID,PERIOD_MONTH,CHECK_FAMILY,SOURCE_FAMILY,EXPECTED,OBSERVED,GAP,"
                     "SEVERITY,ESTIMATED_TAX_EXPOSURE_INR,EVIDENCE,DISCREPANCY_CLASS "
                     "FROM GST_EVIDENCE.V_ALL_EVIDENCE "
                     f"WHERE FACTORY_ID='{factory_id}' ORDER BY PERIOD_MONTH,CHECK_FAMILY LIMIT 200")
    signals = query("SELECT PERIOD_MONTH,CHECK_FAMILY,SOURCE_FAMILY,SEVERITY FROM GST_EVIDENCE.V_FEATURES "
                    f"WHERE FACTORY_ID='{factory_id}' ORDER BY PERIOD_MONTH,CHECK_FAMILY LIMIT 100")
    disposition = query("SELECT PERIOD_MONTH,SOURCE_FAMILY,DISPOSITION FROM GST_EVIDENCE.V_SINGLE_SIGNAL_DISPOSITIONS "
                        f"WHERE FACTORY_ID='{factory_id}' AND SIGNAL_COUNT=1 ORDER BY PERIOD_MONTH LIMIT 12")
    return {"factory_id": factory_id, "timeline": timeline, "evidence": evidence,
            "signals": signals, "dispositions": disposition}


def note(factory_id: str) -> dict:
    payload = case(factory_id)
    evidence = payload["evidence"]
    text = build_case_note(factory_id, evidence)
    return {"factory_id": factory_id, "note": text, "mode": "deterministic fallback",
            "validated": validate_note(text, evidence), "evidence_rows": len(evidence)}


class Handler(BaseHTTPRequestHandler):
    server_version = "GSTEvidenceLocalAPI/1.0"

    def log_message(self, _format, *_args):
        return

    def rate_limited(self) -> bool:
        now = time.monotonic()
        with LOCK:
            bucket = REQUESTS[self.client_address[0]]
            while bucket and bucket[0] < now - RATE_WINDOW_SECONDS:
                bucket.popleft()
            if len(bucket) >= RATE_LIMIT:
                return True
            bucket.append(now)
        return False

    def response(self, status: int, body: dict) -> None:
        encoded = json.dumps(body, default=serialise).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(encoded)

    def record(self, endpoint: str, started: float, sql: str | None = None, rows: int | None = None) -> None:
        with LOCK:
            ACTIVITY.appendleft({"time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                 "endpoint": endpoint, "latency_ms": round((time.monotonic() - started) * 1000, 1),
                                 "sql": sql, "rows": rows})

    def dispatch(self, method: str) -> None:
        if self.rate_limited():
            self.response(HTTPStatus.TOO_MANY_REQUESTS, {"error": "rate limit exceeded"})
            return
        started = time.monotonic()
        parsed = urlparse(self.path)
        try:
            if method == "GET" and parsed.path == "/health":
                body = {"mode": "Live", "time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                        "git_sha": git_sha(), "query_timeout_seconds": TIMEOUT_SECONDS, "row_limit": MAX_ROWS}
            elif method == "GET" and parsed.path == "/queue":
                body = queue(parse_qs(parsed.query))
            elif method == "GET" and parsed.path.startswith("/case/"):
                body = case(parsed.path.rsplit("/", 1)[1])
            elif method == "GET" and parsed.path.startswith("/note/"):
                body = note(parsed.path.rsplit("/", 1)[1])
            elif method == "GET" and parsed.path == "/activity":
                body = {"rows": list(ACTIVITY)}
            elif method == "POST" and parsed.path == "/ask":
                length = int(self.headers.get("Content-Length", "0"))
                if length > 2048:
                    raise ValueError("Request too large.")
                request = json.loads(self.rfile.read(length))
                factory_id = require_factory(str(request.get("factory_id", "")))
                sql = plan_question(str(request.get("question", "")), factory_id, use_llm=False)
                connection = connect(readonly=True)
                try:
                    answer = execute_followup(connection, sql)
                finally:
                    connection.close()
                body = {"intent": next(k for k, v in __import__("src.followup", fromlist=["TEMPLATES"]).TEMPLATES.items() if v.format(factory_id=factory_id) == sql),
                        "sql": sql, "rows": answer, "row_limit": MAX_ROWS, "timeout_seconds": TIMEOUT_SECONDS}
                self.record("/ask", started, sql, len(answer))
                self.response(HTTPStatus.OK, body)
                return
            else:
                self.response(HTTPStatus.NOT_FOUND, {"error": "not found"})
                return
            self.record(parsed.path, started, None, len(body.get("rows", [])) if isinstance(body, dict) else None)
            self.response(HTTPStatus.OK, body)
        except (ValueError, json.JSONDecodeError) as error:
            self.response(HTTPStatus.BAD_REQUEST, {"error": str(error)})
        except Exception as error:  # Never leak credential or driver details to the browser.
            self.response(HTTPStatus.SERVICE_UNAVAILABLE, {"error": "local read-only data source unavailable", "detail": type(error).__name__})

    def do_GET(self):
        self.dispatch("GET")

    def do_POST(self):
        self.dispatch("POST")


def main() -> None:
    port = int(os.getenv("GST_API_PORT", "8765"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"GST Evidence local API listening on http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
