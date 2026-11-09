
from util.db_connection import get_connection


class BaseDAO:

    def run(self, query, values=(), fetch=None):

        connection = get_connection()

        if connection is None:
            return None

        cursor = None

        try:
            cursor = connection.cursor(
                dictionary=fetch in ("one", "all")
            )

            cursor.execute(query, values)

            if fetch == "one":
                return cursor.fetchone()

            if fetch == "all":
                return cursor.fetchall()

            connection.commit()

            return cursor.lastrowid or cursor.rowcount

        except Exception as error:
            connection.rollback()
            print("Database error:", error)
            return None

        finally:
            if cursor:
                cursor.close()

            connection.close()
