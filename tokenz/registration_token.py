from datetime import datetime, timedelta
import jwt
from tokenz import secret_config
from tokenz import tokenz


def generate_tokenz(form: str, key: str):
    try:
        the_key = secret_config.secret_config(section='reg_tokenz')
        my_string = the_key["secret_key"]

        payload = {
            'exp': datetime.utcnow() + timedelta(days=1, seconds=0),
            'iat': datetime.utcnow(),
            'form': form,
            'key': key
        }
        return jwt.encode(
            payload,
            my_string,
            algorithm='HS256'
        )
    except Exception as e:
        return 0


def get_data(auth_tokenz):
    try:
        the_key = secret_config.secret_config(section='reg_tokenz')
        my_string = the_key["secret_key"]
        payload = jwt.decode(auth_tokenz, my_string, algorithms='HS256')
        form = payload['form']
        key = payload['key']

        return {'form': form, 'key': key}

    except jwt.ExpiredSignatureError as e:

        return 0
    except jwt.InvalidtokenzError as e:

        return 0


# This tokenz contains the form and key and password field
def generate_tokenz_verification(form: str, key: str, password: str):
    try:
        the_key = secret_config.secret_config(section='reg_tokenz')
        my_string = the_key["secret_key"]

        payload = {
            'exp': datetime.utcnow() + timedelta(days=2, seconds=0),
            'iat': datetime.utcnow(),
            'form': form,
            'key': key,
            'password': password
        }
        return jwt.encode(
            payload,
            my_string,
            algorithm='HS256'
        )
    except Exception as e:
        return 0


# The return value contains the form and key and password field
def get_data_verification(auth_tokenz):
    try:
        the_key = secret_config.secret_config(section='reg_tokenz')
        my_string = the_key["secret_key"]
        payload = jwt.decode(auth_tokenz, my_string, algorithms='HS256')
        form = payload['form']
        key = payload['key']
        password = payload['password']

        return {'form': form, 'key': key, 'password': password}

    except jwt.ExpiredSignatureError as e:

        return 0
    except jwt.InvalidtokenzError as e:

        return 0

