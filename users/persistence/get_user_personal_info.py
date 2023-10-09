from mongo_conn import mongo_configuration
import pymongo
import json
from bson import json_util
from users.persistence import get_users_db
from tokenz import tokens
from sql_conn import mysql_conn
from subscription import check_subscription


def get(header):
    users_id = tokens.get_id(header)

    if not str(users_id).isalnum():
        return {'Message': 'login in again.', "statusCode": 600}

    conn = mysql_conn.create()
    cursor = conn.cursor()

    key = mongo_configuration.read_config()
    client = pymongo.MongoClient(key["link"])
    personal_information = {"statusCode": 401, "displayName": 0, "email": 0, "phoneNumber": 0}

    # Check if users is subscribed
    check_sub = check_subscription.check(header=header, client=client)
    personal_information.update({"subscription": int(check_sub)})

    db_name = get_users_db.get(users_id)
    db = client[db_name]
    collection = db["personal_information"]

    cursor.execute(f"SELECT * FROM userss WHERE users_id = %s ;", (users_id,))
    data = cursor.fetchall()

    if len(data) == 1:
        for d in data:
            email = str(d[3])
            display_name = str(d[1])
            phone_number = str(d[4])
            locator = str(d[6])
            personal_information.update(
                {"locator": locator, "displayName": display_name, "email": email, "phoneNumber": phone_number})

    res = collection.find({}, {'users_id': 0, '_id': 0, 'locator': 0})
    for r in res:
        x: dict = json.loads(json_util.dumps(r))
        x.update({"statusCode": 200})
        personal_information.update(x)

    client.close()
    return personal_information
