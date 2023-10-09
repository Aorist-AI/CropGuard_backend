from users.persistence import get_user_info
from tokenz import tokens
from tokenz import registration_token
from users.register import update_normal_signup


def update(msg_received, header):
    users_id = tokens.get_id(header)

    if not str(users_id).isalnum():
        return {'Message': 'login in again.', "statusCode": 600}

    else:
        users_data = get_user_info.get(users_id=users_id)
        email = str(users_data['email'])
        phone_number = str(users_data['phone_number'])
        print(email, phone_number)

        key = 0
        form = 0

        if email != "0":
            form = 'email'
            key = email
        elif phone_number != "0":
            form = 'phoneNumber'
            key = phone_number

        reg_tkn = registration_token.generate_tokenz_verification(form=form, key=key, password='123')

        return update_normal_signup.register(msg_received, reg_tkn)
