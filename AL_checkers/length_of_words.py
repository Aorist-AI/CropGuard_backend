from AL_checkers.disallowed_characters import disallowed


def about_length(string: str):
    maximum_length = 750
    if len(string) > maximum_length:
        return string[:maximum_length]
    else:
        return string


def name_length(string: str):
    _string = disallowed(string)
    maximum_length = 25
    if len(_string) > maximum_length:
        return _string[:maximum_length]
    else:
        return _string
