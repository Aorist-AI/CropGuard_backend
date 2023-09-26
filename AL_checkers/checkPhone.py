import json
from sql_connection import mysql_connection


def check_phoneNo(msg_received):
    phoneNo = str(msg_received["phoneNumber"])

    if phoneNo == '0':
        return json.dumps({'phone': '0'})

    conn = mysql_connection.create()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `users` WHERE `phone_number`= %s ;", (phoneNo,))
    row = cursor.fetchall()

    if len(row) != 0:

        conn.close()
        cursor.close()
        return json.dumps({'phone': '1'})

    else:
        conn.close()
        cursor.close()
        return json.dumps({'phone': '0'})
