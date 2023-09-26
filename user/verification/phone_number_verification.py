import random
from sql_connection import mysql_connection
from datetime import datetime
from datetime import timedelta
from sms import send_verification_sms
from checkers import disallowed_characters
from tokenz import registration_token
from user.register import normal_registration
import string


def send(msg_received):
    try:
        phone_number = disallowed_characters.phone_char(str(msg_received['key']))
        password = msg_received['password']

    except KeyError:
        return {"Message": "A key is missing for SMS verification", "statusCode": 401}

    code = random.randint(1000, 9999)

    q = datetime.now().strftime("%Y-%m-%d %H:%M")
    current_date = datetime.strptime(q[2:], '%y-%m-%d %H:%M')

    conn = mysql_connection.create()
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM `users` WHERE phone_number = %s ;""", (phone_number,))
    check_verified = cursor.fetchall()
    if len(check_verified) != 0:
        cursor.close()
        conn.close()
        return {'Message': 'Phone number is verified, kindly log in.', 'statusCode': 401}

    cursor.execute("""SELECT * FROM `users` WHERE phone_number = %s ;""", (phone_number,))
    users = cursor.fetchall()

    if len(users) == 0:
        cursor.execute("SELECT *FROM `reg_verification` WHERE phone_number = %s;", (phone_number,))
        reg_verification = cursor.fetchall()

        if len(reg_verification) == 0:
            res = send_verification_sms.send(phone_number, code)

            if res["statusCode"] == 200:
                cursor.execute("""
               INSERT INTO `reg_verification` (`id`, `email`, `phone_number`, `code`, `date`,
                `counts`, `createdOn`, `state`, `method`) VALUES 
                (NULL, %s , %s , %s , %s , %s , CURRENT_TIMESTAMP, %s , %s );
               """, (0, phone_number, code, str(q), 1, 'unverified', 'phoneNumber'))
                conn.commit()
                # Add registration token to response
                res.update({'token': registration_token.generate_token_verification('phoneNumber', phone_number,
                                                                                    password)})

            cursor.close()
            conn.close()
            return res

        else:
            for r in reg_verification:
                date = datetime.strptime(r[4][2:], '%y-%m-%d %H:%M')
                reg_phone_number = r[2]
                count = r[5]
                end_date = date + timedelta(seconds=30)

                if end_date < current_date:
                    if count < 10:
                        res = send_verification_sms.send(phone_number, code)

                        if res["statusCode"] == 200:
                            cursor.execute("""
                            UPDATE `reg_verification` SET `code`= %s , `date` = %s, `counts` = %s 
                            WHERE `phone_number` = %s ;
                            """, (code, str(q), count + 1, reg_phone_number))
                            conn.commit()
                            # Add registration token to response
                            res.update({'token': registration_token.generate_token_verification('phoneNumber',
                                                                                                phone_number,
                                                                                                password)})

                        cursor.close()
                        conn.close()
                        return res
                    else:
                        return {'Message': 'SMS not sent, you have exceeded allowed amount, kindly use your email',
                                "statusCode": 500}

                return {'Message': "Kindly wait 5 minutes before requesting a new code"
                                   "number", "statusCode": 401}


def verify(msg_received, header):
    reg_token = registration_token.get_data_verification(header)
    if reg_token == 0:
        return {"Message": "Invalid token provided for verification, restart the process.", "statusCode": 401}
    try:
        code = msg_received['code']
        form = reg_token['form']
        key = reg_token['key']
        password = reg_token['password']
    except KeyError:
        return {"Message": "A key is missing for code verification", "statusCode": 401}

    conn = mysql_connection.create()
    cursor = conn.cursor()

    if form.lower() == 'phonenumber':
        cursor.execute("""
                SELECT * FROM `reg_verification` WHERE 	phone_number = %s AND code = %s ; 
                """, (key, code))
        reg_verification = cursor.fetchall()

        new_code = random.randint(1000, 9999)

        if len(reg_verification) == 1:
            cursor.execute("""
                UPDATE `reg_verification` SET `state` = 'verified', code = %s WHERE phone_number = %s AND code = %s ; 
                       """, (new_code, key, code))

            conn.commit()
            cursor.close()
            conn.close()

            x = {
                "subject": "register_normal",
                "displayName": random_string(),
                "about": "I love Tamu!",
                "password": password,
                "location": [],
                "country": "KE",
                "gender": "male",
                "birthday": 763679927000,
                "over18": 1,
                "interestedIn": "female",
                "interest": ['running', 'swimming', 'dancing'],
                # "profile_image": 0
            }
            res = normal_registration.register(x, header)
            # print(reg_token)
            # print(res)
            if res['statusCode'] == 200:
                return {"Message": "Your phone number has been verified", "token": res["token"], "statusCode": 200}

            else:
                # print(res)
                return {"Message": "Your phone has been verified, but there was an error in registering you.",
                        "statusCode": 500}

        else:
            cursor.close()
            conn.close()
            return {"Message": "Wrong details provided", "statusCode": 401}

    else:
        cursor.close()
        conn.close()
        return {"Message": "Wrong form provided", "statusCode": 401}


def random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))
