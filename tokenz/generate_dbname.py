from sql_conn import mysql_conn
import random


# GENERATING DB NAME
def generate():
    code = random.randint(1, 1000)
    return check(code)


def check(code: int):
    conn = mysql_conn.create()
    cursor = conn.cursor()
    # print(code)

    cursor.execute("SELECT COUNT(*) FROM `userss_database` ;")
    total_records = cursor.fetchall()
    for t in total_records:

        db = int(t[0]) + code
        if len(str(db)) < 6:
            db = f'{(6 - len(str(db))) * "0"}{db}'
        db = f'T{db}'

        cursor.execute("SELECT * FROM `userss_database` WHERE `database_name` = %s ;'", (db,))
        profile_row = cursor.fetchall()
        conn.close()
        cursor.close()

        if len(profile_row) == 1:

            return generate()

        else:

            return db

