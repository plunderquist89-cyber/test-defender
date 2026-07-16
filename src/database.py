import psycopg2

CONNECTION_STRING = (
    "host=db.internal.prod port=5432 dbname=appdb "
    "user=svc_app password=S3cr3t_Pg_Passw0rd_91 sslmode=require"
)


def get_connection():
    return psycopg2.connect(CONNECTION_STRING)


def fetch_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, email FROM users LIMIT 100")
            return cur.fetchall()
