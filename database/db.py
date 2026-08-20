import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            dbname=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            cursor_factory=RealDictCursor
        )

    def execute(self, query, params=None, fetch=False):
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params)

                if fetch:
                    result = cur.fetchall()
                else:
                    result = None

                self.conn.commit()
                return result

        except Exception:
            self.conn.rollback()
            raise

    def close(self):
        self.conn.close()