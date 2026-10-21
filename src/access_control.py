"""Idempotent least-privilege setup for evaluation labels."""


def ensure_evaluator_access(conn):
    roles = {row[0] for row in conn.execute('SELECT ROLE_NAME FROM EXA_ALL_ROLES').fetchall()}
    if 'GST_EVALUATOR' not in roles:
        conn.execute('CREATE ROLE GST_EVALUATOR')
    for statement in (
        'GRANT CREATE SESSION TO GST_EVALUATOR',
        'GRANT USAGE ON GST_EVALUATION TO GST_EVALUATOR',
        'GRANT SELECT ON GST_EVALUATION.TRUTH TO GST_EVALUATOR',
    ):
        conn.execute(statement)
