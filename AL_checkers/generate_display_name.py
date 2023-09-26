from AL_checkers import check_display_name
import random


def generate(display_name: str) -> str:
    if check_display_name.check({'displayName': display_name})["statusCode"] == 401:
        number = random.randint(1, 9000)
        if len(str(number)) != 4:
            number = f'{(4 - len(str(number))) * "0"}{number}'

        return generate(f'{display_name}{number}')

    else:
        return display_name
