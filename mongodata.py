from multiprocessing import connection
import pymongo


connections=pymongo.MongoClient(
            "localhost",
            27017
        )
db = connections["scrawled"]
collection_name = db["classes"]

data=collection_name.find()
for item in data:
    print(item['url'])
