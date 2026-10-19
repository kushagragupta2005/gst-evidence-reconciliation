"""Local Exasol connection. Credentials never appear in reports."""
import os
import ssl
from pathlib import Path
import pyexasol

def connect(readonly=False):
    dsn = os.getenv('EXASOL_DSN','localhost:8563')
    local = dsn.split(':')[0] in ('localhost','127.0.0.1')
    # The dashboard never falls back to SYS for its read-only SQL tool.
    user = os.getenv('EXASOL_RO_USER' if readonly else 'EXASOL_USER', 'mcp_readonly' if readonly else 'sys')
    password = os.getenv('EXASOL_RO_PASSWORD' if readonly else 'EXASOL_PASSWORD')
    if not password and local:
        credential = Path.home()/'.exasol-starter-kit/credentials'/('mcp_readonly_password' if readonly else 'personal_sys_password')
        if credential.exists():
            password = credential.read_text().strip()
        else:
            raise RuntimeError('Set Exasol credentials in environment; see README.')
    if not password:raise RuntimeError('Set credentials for the configured Exasol endpoint.')
    opts = dict(dsn=dsn,user=user,password=password,compression=True,autocommit=True)
    if local:
        opts['websocket_sslopt']={'cert_reqs':ssl.CERT_NONE}
    conn=pyexasol.connect(**opts)
    if readonly:
        system={r[0] for r in conn.execute("SELECT PRIVILEGE FROM SYS.EXA_USER_SYS_PRIVS").fetchall()}
        objects={r[0] for r in conn.execute("SELECT PRIVILEGE FROM SYS.EXA_USER_OBJ_PRIVS").fetchall()}
        if not system <= {"CREATE SESSION","SELECT ANY TABLE","USE ANY SCHEMA"} or not objects <= {"SELECT"}:
            conn.close()
            raise RuntimeError("Dashboard credentials must have read-only privileges.")
        conn.execute("ALTER SESSION SET QUERY_TIMEOUT=30")
    return conn

def execute_file(conn, path):
    for statement in Path(path).read_text().split(';'):
        if statement.strip():
            conn.execute(statement)
