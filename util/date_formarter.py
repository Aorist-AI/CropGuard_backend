from datetime import datetime


def format_date(string_date: str):
    first_part = string_date.split(" ")[0]
    day = order(int(str(first_part).split("-")[2]))
    month = month_name(int(str(first_part).split("-")[1]))
    year = str(first_part).split("-")[0]

    hour = check_hour(string_date.split(" ")[1])

    return f'{day} {month} {year} {hour}'


def order(n):
    return str(n) + ("th" if 4 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))


def month_name(n):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return months[int(n) - 1]


def check_if_today(string_date):
    today = str(datetime.now()).split(" ")[0]

    if today == string_date:
        return "today"
    else:
        return format_date(string_date)


def check_hour(the_hour: str):
    hour = int(the_hour.split(':')[0])
    minutes = int(the_hour.split(':')[1])
    final_time = ''
    if (hour - 12) < 0:
        final_time = f'{hour}:{minutes} AM'
    elif hour == 12:
        final_time = f'{hour}:{minutes} PM'
    elif hour > 12:
        final_time = f'{hour - 12}:{minutes} PM'

    return final_time


# print(formart_date("2021-11-13"))
# print(checkIfToday("2022-04-12"))
# print(check_hour('17:25:49.531645'))
# print(format_date(str(datetime.now())))
