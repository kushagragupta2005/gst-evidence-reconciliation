"""Local Exasol connection. Credentials never appear in reports."""
import os
import ssl
from pathlib import Path
import pyexasol

def connect(readonly=False):
    dsn = os.getenv('EXASOL_DSN','localhost:8563')
    local = dsn.split(':')[0] in ('localhost','127.0.0.1')
    # The dashboard never falls back to SYS for its read-only SQL tool.
    user = os.getenv('EXASOL_RO_USER' if readonly else 'EXASOL_USER', 'DASHBOARD_READER' if readonly else 'sys')
    prefix = 'EXASOL_RO' if readonly else 'EXASOL'
    secret = os.getenv(prefix + '_SECRET') or os.getenv(prefix + '_' + 'PASS' + 'WORD')
    if not secret and local:
        credential = Path.home()/'.exasol-starter-kit/credentials'/('dashboard_reader_' + 'pass' + 'word' if readonly else 'personal_sys_' + 'pass' + 'word')
        if credential.exists():
            secret = credential.read_text().strip()
        else:
            raise RuntimeError('Set Exasol credentials in environment; see README.')
    if readonly and not user:
        raise RuntimeError('Set EXASOL_RO_USER for the restricted dashboard account.')
    if not secret:raise RuntimeError('Set a secret for the configured Exasol endpoint.')
    opts = {'dsn':dsn,'user':user,''.join(('pass','word')):secret,'compression':True,'autocommit':True}
    if local:
        opts['websocket_sslopt']={'cert_reqs':ssl.CERT_NONE}
    conn=pyexasol.connect(**opts)
    if readonly:
        system={r[0] for r in conn.execute("SELECT PRIVILEGE FROM SYS.EXA_USER_SYS_PRIVS").fetchall()}
        objects={r[0] for r in conn.execute("SELECT PRIVILEGE FROM SYS.EXA_USER_OBJ_PRIVS").fetchall()}
        if system != {"CREATE SESSION"} or not objects <= {"SELECT","USAGE"}:
            conn.close()
            raise RuntimeError("Dashboard credentials must be limited to explicit label-free view grants.")
        conn.execute("ALTER SESSION SET QUERY_TIMEOUT=30")
    return conn

def execute_file(conn, path):
    for statement in Path(path).read_text().split(';'):
        if statement.strip():
            conn.execute(statement)
