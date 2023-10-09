import random
from datetime import datetime, timedelta
from sql_conn import mysql_conn
from email_handler import send_verification_email
from tokenz import registration_tokenz
from AL_checkers import validEmail
from users.register import normal_registration
import string


def send(msg_received):
    try:
        email = msg_received['key']
        password = msg_received['password']

        if validEmail.valid_email(email) == 0:
            return {"Message": "Invalid Email", "statusCode": 401}

        # form = msg_received['form']

    except KeyError:
        return {"Message": "A key is missing for email verification", "statusCode": 401}

    code = random.randint(1000, 9999)

    q = datetime.now().strftime("%Y-%m-%d %H:%M")
    current_date = datetime.strptime(q[2:], '%y-%m-%d %H:%M')

    conn = mysql_conn.create()
    cursor = conn.cursor()

    # cursor.execute("""SELECT * FROM `userss` WHERE `email` = %s ;""", (email,))
    # check_verified = cursor.fetchall()
    # if len(check_verified) != 0:
    #     cursor.close()
    #     conn.close()
    #     return {'Message': 'Email is verified, kindly log in.', 'statusCode': 200}

    cursor.execute("""SELECT * FROM `userss` WHERE email = %s ;""", (email,))
    userss = cursor.fetchall()

    if len(userss) == 0:
        cursor.execute("SELECT *FROM `reg_verification` WHERE email = %s; ", (email,))
        reg_verification = cursor.fetchall()

        if len(reg_verification) == 0:
            res = send_verification_email.send(email, code)

            if res["statusCode"] == 200:
                cursor.execute("""
                   INSERT INTO `reg_verification` (`id`, `email`, `phone_number`, `code`, `date`,
                    `counts`, `createdOn`, `state`, `method`) VALUES 
                    (NULL, %s , %s , %s , %s , %s , CURRENT_TIMESTAMP, %s , %s );
                   """, (email, 0, code, str(q), 1, 'unverified', 'email'))
                conn.commit()
                # Add registration tokenz to response
                res.update({'tokenz': registration_tokenz.generate_tokenz_verification('email', email, password)})

            cursor.close()
            conn.close()
            return res

        else:
            for r in reg_verification:
                date = datetime.strptime(r[4][2:], '%y-%m-%d %H:%M')
                reg_email = r[1]
                count = r[5]
                end_date = date + timedelta(seconds=30)

                if end_date < current_date:
                    # For testing
                    if count < 10000:
                        res: dict = send_verification_email.send(email, code)

                        if res["statusCode"] == 200:
                            cursor.execute("""
                                UPDATE `reg_verification` SET `code`= %s , `date` = %s, `counts` = %s 
                                WHERE `email` = %s ;
                                """, (code, str(q), count + 1, reg_email))
                            conn.commit()

                            # Add registration tokenz to response
                            res.update({'tokenz': registration_tokenz.generate_tokenz_verification('email', email,password)})

                        cursor.close()
                        conn.close()
                        return res
                    else:
                        cursor.close()
                        conn.close()
                        return {'Message': "Email not sent, you have exceeded allowed amount, kindly use your phone "
                                           "number", "statusCode": 500}
                else:
                    cursor.close()
                    conn.close()
                    return {'Message': "Kindly wait 5 minutes before requesting a new code"
                                       "number", "statusCode": 401}
    else:
        cursor.close()
        conn.close()
        return {'Message': 'Email is already taken.', 'statusCode': 200}


def verify(msg_received, header):
    reg_tokenz = registration_tokenz.get_data_verification(header)
    # print(reg_tokenz)
    if reg_tokenz == 0:
        return {"Message": "Invalid tokenz provided for verification, restart the process.", "statusCode": 401}

    try:
        code = msg_received['code']
        form = reg_tokenz['form']
        key = reg_tokenz['key']
        password = reg_tokenz['password']
        # print(form, key)
    except KeyError:
        return {"Message": "A key is missing for code verification", "statusCode": 401}

    conn = mysql_conn.create()
    cursor = conn.cursor()

    if form.lower() == 'email':
        cursor.execute("""
        SELECT * FROM `reg_verification` WHERE email = %s AND code = %s ; 
        """, (key, code))
        reg_verification = cursor.fetchall()

        new_code = random.randint(1000, 9999)

        if len(reg_verification) == 1:
            cursor.execute("""
            UPDATE `reg_verification` SET `state` = 'verified' , code = %s WHERE email = %s AND code = %s ; 
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
            res = dict(normal_registration.register(x, header))
            # print(res)
            if res["statusCode"] == 200:
                return {"Message": "Your email has been verified", "tokenz": res["tokenz"], "statusCode": 200}

            else:
                return {"Message": "Your email has been verified, but there was an error in registering you.",
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