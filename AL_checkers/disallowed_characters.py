import re


def disallowed(string: str):
    # This is for names
    disallowed_characters = "^}{=~,[<>]/*-;+/:()%$#@!|/?_\'\"`.1234567890"
    _name = string.lower()
    for character in disallowed_characters:
        _name = _name.replace(character, "")

    __name = list(_name)
    first_character = _name[0].upper()
    __name[0] = first_character
    _name = ''.join(__name)

    return _name


def not_allowed(string: str):
    # This is for strings
    disallowed_characters = "^}{=~,[<>]/*-;+/:()%$#@!|/?_\'\"`.1234567890"
    _name = string
    for character in disallowed_characters:
        _name = _name.replace(character, "")

    return _name


def phone_char(string: str):
    # This is for phone numbers
    disallowed_characters = "^}{=~,[<>]/*-;/:()%$#@!|/?_\'\"`"
    _number = string
    for character in disallowed_characters:
        _number = _number.replace(character, "")

    _number = re.sub('[A-Za-z]', '', _number)

    return _number

