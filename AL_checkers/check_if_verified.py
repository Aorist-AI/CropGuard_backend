from sql_conn import mysql_conn


def check(key, form):
    conn = mysql_conn.create()
    cursor = conn.cursor()
    value = 0

    if form == 'email':
        cursor.execute("SELECT *FROM `reg_verification` WHERE email = %s AND state = 'verified' ;", (key,))
        verification = cursor.fetchall()
        if len(verification) == 1:
            value = 1

    elif form == 'phoneNumber':
        cursor.execute("SELECT * FROM `reg_verification` WHERE phone_number = %s AND state = 'verified' ;", (key,))
        verification = cursor.fetchall()
        if len(verification) == 1:
            value = 1

    cursor.close()
    conn.close()
    return value
