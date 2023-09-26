from datetime import datetime, timedelta


def calculate(birthday):
    current_timestamp = datetime.strptime(str(datetime.now()).split(" ")[0], '%Y-%m-%d')
    date = datetime(1970, 1, 1) + timedelta(seconds=birthday / 1000)
    # birthday_date = datetime.strptime(str(datetime.fromtimestamp(birthday / 1000))[2:].split(" ")[0], '%y-%m-%d')
    birthday_date = datetime.strptime(str(date).split(" ")[0], '%Y-%m-%d')
    age = current_timestamp - birthday_date

    # print(current_timestamp)
    # print(date)
    return int(age.days / 365)


# print(calculate(int(1047209849000)))
# print(calculate(int(-5730144000)))
# date = datetime(1970, 1, 1) + timedelta(seconds=-625421856000/1000)
# print(date)
# print(datetime.now())