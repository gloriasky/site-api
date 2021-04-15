from pymongo import MongoClient
from constants import *

client = MongoClient(MONGO_HOST)
db = client[DB]
table = db[PROJECTS_LINKS_TABLE]


def get_projects():
    return list(table.find({'isActive': True}, {'_id': 0}))


def save_project(project: dict):
    table.insert_one(project)
