from pymongo import MongoClient
from constants import *

client = MongoClient(MONGO_HOST)
db = client[DB]
table = db[CONTACT_LINKS_TABLE]


def get_links():
    return list(table.find({}, {'_id': 0}))

