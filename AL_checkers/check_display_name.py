from sql_conn import mysql_conn


def check(msg_received):
    try:
        display_name = str(msg_received['displayName'])

    except KeyError:
        return {"Message": "A key is missing for checking display name", "statusCode": 401}

    if display_name == '0':
        return {"Message": "Display name is available", "statusCode": 200}

    conn = mysql_conn.create()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM `userss` WHERE display_name = %s ;', (display_name,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if len(data) == 0:
        return {"Message": "Display name is available", "statusCode": 200}

    else:
        return {"Message": "Display name has been taken", "statusCode": 401}



