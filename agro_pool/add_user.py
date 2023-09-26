from mongodb_connection import mongo_configuration
import pymongo


def add(user_data: dict):
    #  format {
    #     'user_id'
    #     'gender'
    #     'interested_in'
    #     'country'
    # }

    key = mongo_configuration.read_config()
    client = pymongo.MongoClient(key["link"])

    # Tamu pool
    db = client[user_data['country']]
    collection = db[user_data['gender']]

    collection.insert_one(user_data)
    client.close()


def remove_update(user_data: dict):
    key = mongo_configuration.read_config()
    client = pymongo.MongoClient(key["link"])

    # Old Tamu pool
    db = client[user_data['old_country']]
    old_collection = db[user_data['old_gender']]

    # Tamu pool
    db = client[user_data['country']]
    collection = db[user_data['gender']]

    user_data.pop('old_country')
    user_data.pop('old_gender')

    old_collection.delete_one({'user_id': user_data['user_id']})
    collection.insert_one(user_data)
    client.close()
