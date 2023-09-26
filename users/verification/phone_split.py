import pymongo
from mongo_conn import mongo_configuration


def check(string: str):
    key = mongo_configuration.read_config()
    client = pymongo.MongoClient(key["link"])
    db_name = "tamu"
    collection = client[db_name]["reg_phone_numbers"]

    country_code = string.split("-")[0]  # .replace("+", "")
    first_char = string.split("-")[1][:1]
    phone_number = string.split("-")[1][:1]
    if first_char == 0:
        phone_number = phone_number.split("-")[1][1:]

    if collection.count_documents({"countryCode": country_code, "phoneNumber": phone_number}) != 0:
        client.close()
        return 1
    else:
        client.close()
        return 0

# x = "12-078212".split("-")[1][1:]
# print(x)
