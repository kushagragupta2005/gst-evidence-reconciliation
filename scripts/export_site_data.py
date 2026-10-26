"""Export audited, public snapshot data for the static officer interface.

The default mode never connects to Exasol.  ``--live`` adds label-free queue,
case, and disposition snapshots through the restricted account only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "website" / "data"


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text())


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def dump(name: str, value: object) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")


def rows(statement) -> list[dict]:
    columns = [column.lower() for column in statement.column_names()]
    return [dict(zip(columns, row)) for row in statement.fetchall()]


def live_snapshot() -> dict:
    # Import only in live mode so a static snapshot can be exported offline.
    from src.db import connect

    conn = connect(readonly=True)
    try:
        queue = rows(conn.execute("""
            SELECT FACTORY_ID, PERIOD_MONTH, SIGNAL_COUNT,
                   WEAKEST_LINK_NORMALISED_GAP, ESTIMATED_TAX_EXPOSURE_INR, STATUS
            FROM GST_EVIDENCE.V_RANKED_CASES
            WHERE STATUS='prioritise'
            ORDER BY SIGNAL_COUNT DESC, WEAKEST_LINK_NORMALISED_GAP DESC,
                     ESTIMATED_TAX_EXPOSURE_INR DESC, FACTORY_ID
            LIMIT 200
        """))
        dispositions = rows(conn.execute("""
            SELECT FACTORY_ID, PERIOD_MONTH, SOURCE_FAMILY, DISPOSITION
            FROM GST_EVIDENCE.V_SINGLE_SIGNAL_DISPOSITIONS
            WHERE SIGNAL_COUNT=1
            ORDER BY PERIOD_MONTH, FACTORY_ID
            LIMIT 200
        """))
        factory_ids = sorted({row["factory_id"] for row in queue[:12]})
        cases = {}
        for factory_id in factory_ids:
            timeline = rows(conn.execute(
                "SELECT PERIOD_MONTH,SIGNAL_COUNT,TOTAL_SEVERITY,WEAKEST_LINK_NORMALISED_GAP,"
                "ESTIMATED_TAX_EXPOSURE_INR,STATUS FROM GST_EVIDENCE.V_RANKED_CASES "
                f"WHERE FACTORY_ID='{factory_id}' ORDER BY PERIOD_MONTH LIMIT 12"))
            evidence = rows(conn.execute(
                "SELECT FACTORY_ID,PERIOD_MONTH,CHECK_FAMILY,SOURCE_FAMILY,EXPECTED,OBSERVED,GAP,"
                "SEVERITY,ESTIMATED_TAX_EXPOSURE_INR,EVIDENCE,DISCREPANCY_CLASS "
                "FROM GST_EVIDENCE.V_ALL_EVIDENCE "
                f"WHERE FACTORY_ID='{factory_id}' ORDER BY PERIOD_MONTH,CHECK_FAMILY LIMIT 200"))
            cases[factory_id] = {"timeline": timeline, "evidence": evidence}
        return {"queue": queue, "dispositions": dispositions, "cases": cases}
    finally:
        conn.close()


def main() -> None:
    global OUT
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true", help="also snapshot label-free live Exasol views")
    parser.add_argument("--out", type=Path, default=OUT, help="directory for generated JSON")
    args = parser.parse_args()
    OUT = args.out
    primary = load("results.json")
    dev = load("reports/v3_a_calibration.json")
    confirmation = load("reports/v3_c_results.json")
    disposition_b = load("reports/v3_b_dispositions.json")
    disposition_c = load("reports/v3_c_dispositions.json")
    performance = {
        "benchmark_small": load("reports/benchmark_small.json"),
        "benchmark_full": load("reports/benchmark_full.json"),
        "pandas_full": load("reports/pandas_full.json"),
        "concurrency": load("reports/concurrency.json"),
        "live_smoke": load("reports/live_smoke.json"),
        "duckdb": {"status": "not measured", "reason": "No committed DuckDB benchmark artifact exists."},
    }
    evaluation = {
        "ablation": load("reports/site_ablation.json"),
        "dev_v3_a": dev,
        "heldout_v3_b": primary,
        "heldout_v3_c": confirmation,
        "dispositions": {"v3_b": disposition_b, "v3_c": disposition_c},
        "not_measured": {
            "per_decoy_fpr_before_after_verified_clearing": "No committed paired artifact exists.",
            "sophisticated_forger_scenario": "Not implemented or evaluated in a preregistered suite.",
            "evasive_recall_with_without_stock_aware": "No committed paired artifact exists.",
            "ablation_confidence_intervals": "Post-hoc replay supplies point estimates only.",
            "prevalence_2_percent": "No committed 2% prevalence artifact exists.",
        },
    }
    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "git_sha": git_sha(),
        "results_sha256": sha256(ROOT / "results.json"),
        "source": "committed results.json and reports/*.json",
        "mode": "snapshot",
        "live_snapshot": False,
    }
    dump("manifest.json", manifest)
    dump("evaluation.json", evaluation)
    dump("performance.json", performance)
    dump("snapshot.json", {"queue": [], "dispositions": [], "cases": {}, "status": "offline snapshot; start make api for live label-free case data"})
    if args.live:
        dump("snapshot.json", live_snapshot())
        manifest["live_snapshot"] = True
        dump("manifest.json", manifest)
    bundle = {name: json.loads((OUT / (name + ".json")).read_text()) for name in ("manifest", "evaluation", "performance", "snapshot")}
    bundle["examples"] = load("reports/site_examples.json")
    bundle["manifest"]["repo_url"] = subprocess.check_output(["git", "remote", "get-url", "origin"], cwd=ROOT, text=True).strip().removesuffix(".git")
    (OUT.parent / "data.js").write_text("window.__SNAPSHOT__ = " + json.dumps(bundle, default=str).replace("<", "\\u003c") + ";\n")


if __name__ == "__main__":
    main()
