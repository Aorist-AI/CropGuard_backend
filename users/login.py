from sql_conn import mysql_conn
import bcrypt

def login(msg_received):
    try:
        key = msg_received['key']
        plain_password = msg_received['password']
    except KeyError as e:
        return {'Message': 'A key for login is missing', 'Error': str(e), 'statusCode': 401}
    try:
        
        conn = mysql_conn.create()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users where phone_number = %s OR email = %s  ;", (key, key))
        row = cursor.fetchall()

        # while row is not None:
        hashed_password = ""
        if len(row) == 1:
            for record in row:
                # print(record)
                hashed_password = str(record[5]).encode('utf8')

            if bcrypt.checkpw(plain_password, hashed_password):

                cursor.close()
                conn.close()

                return {"Message": "Sign in successful", "statusCode": 200}

            else:
                cursor.close()
                conn.close()
                return {"Message": "wrong login details provided", "statusCode": 404}

        else:
            cursor.close()
            conn.close()
            return {"Message": "wrong login details provided", "statusCode": 404}
        
    except Exception as e:
        return{'Error': str(e), "statusCode": 600}
