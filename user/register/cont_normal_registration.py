from user.persistence import get_user_info
from tokenz import tokens
from tokenz import registration_token
from user.register import update_normal_registration


def update(msg_received, header):
    user_id = tokens.get_id(header)

    if not str(user_id).isalnum():
        return {'Message': 'login in again.', "statusCode": 600}

    else:
        user_data = get_user_info.get(user_id=user_id)
        email = str(user_data['email'])
        phone_number = str(user_data['phone_number'])
        print(email, phone_number)

        key = 0
        form = 0

        if email != "0":
            form = 'email'
            key = email
        elif phone_number != "0":
            form = 'phoneNumber'
            key = phone_number

        reg_tkn = registration_token.generate_token_verification(form=form, key=key, password='123')

        return update_normal_registration.register(msg_received, reg_tkn)
