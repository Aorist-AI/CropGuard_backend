from sql_connection import mysql_connection
from tokenz import tokens
import bcrypt
from user.persistence import get_user_info
from subscription import check_subscription


def login(msg_received):
    try:
        key = str(msg_received["key"]).replace(" ", "").replace("_deleted", "")
        plain_password = str(msg_received["password"]).encode('utf-8')
    except KeyError:
        return {"Message": "A key is missing", "statusCode": 401}

    user_id = " "

    conn = mysql_connection.create()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users where phone_number = %s OR email = %s  ;", (key, key))
    row = cursor.fetchall()

    # while row is not None:
    locator = ""
    hashed_password = ""
    if len(row) == 1:
        for record in row:
            # print(record)

            user_id = int(record[0])
            locator = str(record[6])
            hashed_password = str(record[5]).encode('utf8')

        if bcrypt.checkpw(plain_password, hashed_password):

            tkn = str(tokens.generate_token(user_id, locator))
            user_data = get_user_info.get(user_id=user_id)
            registration = user_data['personalInformation']['registration']
            check_sub = check_subscription.check(header=tkn)
            cursor.close()
            conn.close()

            return {"Message": "Sign in successful", "token": tkn, "registration": registration,
                    "subscription": int(check_sub),
                    "statusCode": 200}

        else:
            cursor.close()
            conn.close()
            return {"Message": "wrong login details provided", "statusCode": 404}

    else:
        cursor.close()
        conn.close()
        return {"Message": "wrong login details provided", "statusCode": 404}

#
# print(login({
#     "key": '+254713234177',
#     'password': 'password'
# }))
