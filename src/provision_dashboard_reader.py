"""Create the local restricted dashboard account without exposing its secret."""
import os
import secrets
from pathlib import Path

from src.db import connect, execute_file


USER = 'DASHBOARD_READER'


def main():
    credential = Path.home() / '.exasol-starter-kit' / 'credentials' / ('dashboard_reader_' + 'pass' + 'word')
    # Reuse the local secret when the account was created by a prior run.  A
    # fresh checkout shares the local Personal instance, so generating a new
    # secret here would leave the existing account and credential file out of
    # sync.
    secret = os.getenv('EXASOL_RO_SECRET') or (credential.read_text().strip() if credential.exists() else secrets.token_urlsafe(32))
    admin = connect()
    try:
        try:
            admin.execute(f'CREATE USER {USER} IDENTIFIED BY "{secret}"')
        except Exception as exc:
            if 'already exists' not in str(exc).lower() and 'conflicts with another user or role' not in str(exc).lower():
                raise
        # This also repairs a stale local credential after an interrupted
        # setup. The secret is never written to stdout or a project file.
        admin.execute(f'ALTER USER {USER} IDENTIFIED BY "{secret}"')
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
        credential.parent.mkdir(parents=True, exist_ok=True)
        credential.write_text(secret + '\n')
        credential.chmod(0o600)
    print(f'{USER} configured; label-free view grants are applied after reconciliation views exist. Secret was not printed.')


if __name__ == '__main__':
    main()
