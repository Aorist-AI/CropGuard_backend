from token import picture_code
from sql_conn import mysql_conn


# GENERATING LOCATOR
def generate():
    code = str(picture_code.users_locator())
    return check(code)


def check(code: str):
    conn = mysql_conn.create()
    cursor = conn.cursor()
    # print(code)

    cursor.execute("SELECT * FROM `userss` WHERE `locator` = %s ;'", (code,), multi=True)
    profile_row = cursor.fetchall()
    conn.close()
    cursor.close()

    if len(profile_row) == 1:

        return generate()

    else:

        return code
