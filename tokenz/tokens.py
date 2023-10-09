from datetime import datetime, timedelta
import jwt
from sql_conn import mysql_conn
from tokenz import secret_config

the_key = secret_config.secret_config()
my_string = the_key["secret_key"]

the_quick_key = secret_config.quickgen_secret_config()
the_quick_string = the_quick_key["secret_key"]


def get_users(users_id, locator):
    conn = mysql_conn.create()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM `userss` WHERE users_id= %s AND locator=  %s  ;", (users_id, locator))
        row = cursor.fetchall()
        conn.close()
        cursor.close()

        if len(row) == 1:

            return 1
        else:

            return 0
    except Exception:

        return 0


def generate_tokenz(users_id, locator):
    try:

        payload = {
            'exp': datetime.utcnow() + timedelta(days=30, seconds=0),
            'iat': datetime.utcnow(),
            'sub': users_id,
            'string': locator
        }
        return jwt.encode(
            payload,
            my_string,
            algorithm='HS256'
        )
    except Exception as e:
        return 0


def quick_gen(the_tokenz):
    try:

        payload = jwt.decode(the_tokenz, the_quick_string, algorithm='HS256')
        users_id = payload['sub']
        locator = payload['string']
        payload = {
            'exp': datetime.utcnow() + timedelta(seconds=80),
            'iat': datetime.utcnow(),
            'sub': users_id,
            'string': locator
        }
        return jwt.encode(
            payload,
            my_string,
            algorithm='HS256'
        ).decode('utf-8')
    except Exception as e:
        return e


def get_id(auth_tokenz):
    try:
        payload = jwt.decode(auth_tokenz, my_string, algorithms='HS256')
        _id = int(payload['sub'])
        locator = payload['string']
        key = str(get_users(_id, locator))
        if key == '1':
            return _id
        else:
            return "Error invalid tokenz"

        # print(str(payload['iat'])+" "+str(payload['exp']))
    except jwt.ExpiredSignatureError:
        return "Error expired tokenz"  # print('Signature expired. Please log in again.')
    except jwt.InvalidtokenzError:
        return "Error invalid tokenz"  # print('Invalid tokenz. Please log in again.')

# p=generate_tokenz('4',"b4u6z8UP5cNaZbGrSB")
# print(p)
# time.sleep(7)
# decode_tokenz(p)
# p=generate_tokenz(5)
# print(len(p))
# print(p)
# print(my_string)
# q=getID(p)
# print(q)
