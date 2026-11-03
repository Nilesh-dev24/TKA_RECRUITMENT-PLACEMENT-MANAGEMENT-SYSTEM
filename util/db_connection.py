import os
import mysql.connector

def get_connection():
    try:
        print("Connecting to MySQL...", flush=True)

        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "rpms_db"),
            port=int(os.getenv("DB_PORT", "3306")),
            connection_timeout=5,
            use_pure=True
        )

        print("Connection attempt completed!", flush=True)
        return connection

    except Exception as error:
        print("Database connection failed:", repr(error), flush=True)
        return None