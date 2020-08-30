import psycopg2
from config import DB_USER_NAME, DB_USER_PASSWORD, DATABASE_NAME


# Абстрактный класс для всех сущностей
class BackendMixin:
    @property
    def _con(self):
        return psycopg2.connect(
            host="localhost",
            user=DB_USER_NAME,
            password=DB_USER_PASSWORD,
            dbname=DATABASE_NAME,
        )

    @property
    def _cursor(self):
        return self._con.cursor()

    def get_all(self, table):
        cursor = self._cursor
        cursor.execute("select * from " + table)
        result = cursor.fetchall()
        self._con.commit()
        self._con.close()
        return result


if __name__ == "__main__":
    pass
