from pymongo import MongoClient
from src.settings import *

# NOTE https://stackoverflow.com/questions/41607517/do-i-need-to-close-pymongo-session
class mongo():
    conn = None

    def __init__(self):
        self.connect()

    @classmethod
    def connect(self):
        if self.conn is None:
            self.conn = MongoClient(MONGO_URI)
            self.conn = self.conn[MONGO_DATABASE]
        return self.conn

    def find(self, collection, **kwargs):
        return(list(self.conn[collection].find(**kwargs)))
    
    def find_distinct(self, collection, var, **kwargs):
        return(list(self.conn[collection].find(**kwargs).distinct(var)))

    def delete_one(self, collection, document):
        self.conn[collection].delete_one(document)

    def insert_one(self, collection, document):
        self.conn[collection].insert_one(document)

    def update_one(self, collection, filter, doc, upsert=True):
        self.conn[collection].update(filter, doc, upsert=upsert)
