#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all



if __name__ == "__main__":
    mongo_user = "root"
    mongo_pass = "2003"
    mongo_host = "127.0.0.1"
    mongo_port = "27017"
    mongo_db = "my_db"

    connection = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}"
    client = MongoClient(connection)
    school_collection = client[mongo_db]['school']
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))