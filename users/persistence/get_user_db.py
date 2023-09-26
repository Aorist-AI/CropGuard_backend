from sql_conn import mysql_conn


def get(users_id):
    conn = mysql_conn.create()
    cursor = conn.cursor()
    db_name = ''

    cursor.execute("SELECT * FROM userss_database WHERE users_id = %s ;", (users_id,))
    users_db = cursor.fetchall()

    cursor.close()
    conn.close()
    for db in users_db:
        db_name = db[1]

    return db_name
