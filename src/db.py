"""Local Exasol connection. Credentials never appear in reports."""
import os
import ssl
from pathlib import Path
import pyexasol

def connect(readonly=False):
    dsn = os.getenv('EXASOL_DSN','localhost:8563')
    local = dsn.split(':')[0] in ('localhost','127.0.0.1')
    # The dashboard never falls back to SYS for its read-only SQL tool.
    user = os.getenv('EXASOL_RO_USER' if readonly else 'EXASOL_USER', 'GST_READER' if readonly else 'sys')
    password = os.getenv('EXASOL_RO_PASSWORD' if readonly else 'EXASOL_PASSWORD')
    if not password:
        credential = Path('data/generated/reader_password') if readonly else Path.home()/'.exasol-starter-kit/credentials/personal_sys_password'
        if credential.exists():
            password = credential.read_text().strip()
        else:
            raise RuntimeError('Set Exasol credentials in environment; see README.')
    opts = dict(dsn=dsn,user=user,password=password,compression=True,autocommit=True)
    if local:
        opts['websocket_sslopt']={'cert_reqs':ssl.CERT_NONE}
    return pyexasol.connect(**opts)

def execute_file(conn, path):
    for statement in Path(path).read_text().split(';'):
        if statement.strip():
            conn.execute(statement)
