print("Starting database test...")

from util.db_connection import get_connection

print("Testing MySQL connection...")

connection = get_connection()

if connection is None:
    print("Connection object is None. Check database settings.")

else:
    print("Connection object created!")

    if connection.is_connected():
        print("MySQL Connected Successfully!")
    else:
        print("MySQL is not connected.")

    connection.close()
    print("Connection closed.")