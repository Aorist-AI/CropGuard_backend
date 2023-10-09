import json
from AL_checkers import checkEmail, checkPhone
from sql_conn import mysql_conn
from mongo_conn import mongo_configuration
import pymongo
from tokenz import generate_locator, generate_dbname, tokens
import bcrypt
from AL_checkers.disallowed_characters import disallowed, not_allowed, phone_char
from AL_checkers.validEmail import valid_email
from AL_checkers import check_if_verified, age_calculator
from AL_checkers.generate_display_name import generate
from AL_checkers.length_of_words import name_length, about_length
from datetime import datetime, timedelta
from tokenz import registration_token
from agro_pool import add_user
# from referral import set_referral_code  # , add_referred


def register(msg_received, header):
    reg_tokenz = registration_token.get_data(header)
    if reg_tokenz == 0:
        return {"Message": "Invalid tokenz provided for verification", "statusCode": 401}

    try:

        display_name = generate(name_length(str(msg_received["displayName"]))).strip()
        about = about_length(str(msg_received["about"]))
        form = reg_tokenz['form']  # str(msg_received['form']).lower()
        key = str(reg_tokenz['key']).lower().strip()  # str(msg_received['key']).strip()
        email = str(0)
        phone_number = str(0)

        try:
            password = bcrypt.hashpw(msg_received["password"].encode("utf-8"), bcrypt.gensalt())
        except Exception as e:
            # Handle the exception appropriately
            # print(f"Error hashing password: {e}")
            return {"Message": f"Error hashing password: {e}"}

        password = bcrypt.hashpw(msg_received["password"].encode("utf-8"), bcrypt.gensalt())
        location = (msg_received['location'])  # [lon,lat,town:'']
        country = disallowed(str(msg_received['country'])).upper()  # Will be generated from location data

        gender = not_allowed(str(msg_received['gender']).strip()).lower()
        birthday = int(msg_received['birthday'])  # timestamp format in milliseconds
        age = age_calculator.calculate(birthday)
        over_18 = int(msg_received['over18'])  # 0 1
        interested_in = not_allowed(str(msg_received['interestedIn'])).strip().lower()  #
        interest = msg_received['interest']  # list

        ref_code = 0

        profile_image = 'https://profilephoto.tamu.dating'

        try:
            profile_image = f'https://profilephoto.tamu.dating/{msg_received["profile_image"]}'

        except KeyError:
            pass

        if form == 'email':
            email = key
            checkm = json.loads(checkEmail.check_email({'email': email}))
            if valid_email(email) == 0:
                return {"Message": "Invalid Email", "statusCode": 401}

            if checkm["email"] == '1':
                return {"Message": "email already in use.", "statusCode": 401}

        elif form == 'phoneNumber':
            phone_number = phone_char(key)
            checkp = json.loads(checkPhone.check_phoneNo({"phoneNumber": phone_number}))
            if len(phone_number) < 9:
                return {"Message": "Invalid phone number", "statusCode": 401}

            if checkp["phone"] == '1':
                return {"Message": "phone number already in use.", "statusCode": 401}
        else:
            return {"Message": "Invalid form type", "statusCode": 401}

    except KeyError:
        return {"Message": "A key is missing for registrations", "statusCode": 401}

    if age < 18:
        return {"Message": "You should be 18 years old or above to join Tamu.", "statusCode": 401}

    if check_if_verified.check(key, form) == 0:
        return {"Message": f"The {form} is not verified.", "statusCode": 401}

    else:

        conn = mysql_conn.create()
        cursor = conn.cursor()

        db_key = mongo_configuration.read_config()
        client = pymongo.MongoClient(db_key["link"])

        try:
            # Create an account for the users
            locator = str(generate_locator.generate())
            db_name = generate_dbname.generate()
            cursor.execute("""
            INSERT INTO `userss` (`users_id`, `display_name`, `what_i_do`, `email`, `phone_number`, `password`, 
            `locator`,`location`, `date`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP);""",
                           (display_name, '0', email, phone_number, password, locator, 'KE'))

            conn.commit()
            if form == 'phoneNumber':
                form = "phone_number"
            # print(form, key)
            cursor.execute(f"SELECT * FROM `userss` WHERE {form} = %s ;", (key,))
            row = cursor.fetchall()
            tkn = ''

            # Create the database
            for record in row:
                users_id = int(record[0])
                # referral_code = set_referral_code.add({'users_id': users_id, 'locator': locator})["referral_code"]

                cursor.execute("""
                            INSERT INTO `userss_database` (`database_id`, `database_name`, `users_id`, `locator`, `date`)
                             VALUES (NULL, %s , %s , %s , CURRENT_TIMESTAMP);
                            """, (db_name, users_id, locator))

                db = client[db_name]
                collection = db["personal_information"]
                x = {
                    'users_id': int(users_id),
                    'locator': locator,
                    'gender': gender,
                    'location': [],  # [{'longitude':1234,'latitude':1234,'address':}]
                    'about': about,
                    'birthday': str(datetime(1970, 1, 1) + timedelta(seconds=birthday / 1000)).split(" ")[0],
                    'birthday_timestamp': birthday,
                    'age': age,
                    'over_18': over_18,
                    'interested_in': interested_in,
                    'interest': interest,
                    'profile_image': profile_image,
                    'country': country,
                    'referred_by': 0,
                    'registration': 0
                }
                collection.insert_one(x)

                # Add users to pool
                pool_data = {
                    'users_id': users_id,
                    'locator': locator,
                    'gender': gender,
                    'interested_in': interested_in,
                    'country': country,
                    'mood': ''
                }
                add_user.add(pool_data)

                # If referred
                if ref_code != 0:
                    try:
                        ref_code = str(msg_received["referralCode"]).replace(" ", "")
                        # add_referred.add({'referral_code': ref_code, 'locator': locator})
                    except KeyError:
                        pass

                tkn = str(tokens.generate_tokenz(users_id, locator))

            conn.close()
            cursor.close()
            client.close()
            return {"Message": "Account created", "tokenz": tkn, "statusCode": 200}

        except TypeError:
            client.close()
            conn.close()
            cursor.close()
            return {"TypeError": "Account not created", "statusCode": 500}
