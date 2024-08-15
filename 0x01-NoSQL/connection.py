import pymongo
mongo_user = "root"
mongo_pass = "2003"
mongo_host = "127.0.0.1"
mongo_port = "27017"
mongo_db = "my_db"

connection = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}"
client = pymongo.MongoClient(connection)
school_collection = client[mongo_db]['school']