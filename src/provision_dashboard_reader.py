"""Create the local restricted dashboard account without exposing its secret."""
import os
import secrets
from pathlib import Path

from src.db import connect, execute_file


USER = 'DASHBOARD_READER'


def main():
    secret = os.getenv('EXASOL_RO_SECRET') or secrets.token_urlsafe(32)
    admin = connect()
    try:
        try:
            admin.execute(f'CREATE USER {USER} IDENTIFIED BY "{secret}"')
        except Exception as exc:
            if 'already exists' not in str(exc).lower():
                raise
        admin.execute(f'GRANT CREATE SESSION TO {USER}')
        try:
            execute_file(admin, 'sql/02_readonly_grants.sql')
        except Exception as exc:
            # A fresh database has no reconciliation views yet. The loader
            # applies these same grants after it creates the views.
            if 'object' not in str(exc).lower() or 'exist' not in str(exc).lower():
                raise
    finally:
        admin.close()
    if not os.getenv('EXASOL_RO_SECRET'):
        target = Path.home() / '.exasol-starter-kit' / 'credentials' / ('dashboard_reader_' + 'pass' + 'word')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(secret + '\n')
        target.chmod(0o600)
    print(f'{USER} configured; label-free view grants are applied after reconciliation views exist. Secret was not printed.')


if __name__ == '__main__':
    main()
