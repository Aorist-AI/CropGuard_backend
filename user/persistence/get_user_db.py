from sql_connection import mysql_connection


def get(user_id):
    conn = mysql_connection.create()
    cursor = conn.cursor()
    db_name = ''

    cursor.execute("SELECT * FROM users_database WHERE user_id = %s ;", (user_id,))
    user_db = cursor.fetchall()

    cursor.close()
    conn.close()
    for db in user_db:
        db_name = db[1]

    return db_name
