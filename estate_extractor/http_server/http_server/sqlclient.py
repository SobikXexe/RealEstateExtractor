import psycopg2 as pg
from os import getenv

class SQLClient:
    
    items : list[list[str, str]] = []
    next_item_idx = 0

    def refresh_data(self) -> None:
        conn = None
        cur = None
        try:
            conn = pg.connect(host="real_estate_db", port="5432", user=getenv('POSTGRES_USER'), password=getenv('POSTGRES_PASSWORD'), dbname=getenv('POSTGRES_DB'))
            cur = conn.cursor()
            query = "SELECT title, photo FROM flat;"
            cur.execute(query)
            self.items = cur.fetchall()

        except:
            print("Database not ready.")
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()

        self.next_item_idx = 0
        pass

    def get_data(self) -> list[list[str, str]]:
        return self.items

