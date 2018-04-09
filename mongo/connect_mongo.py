import pymongo
from pymongo import MongoClient

def connect_to_mongo(host ='', port = 27017, database = '', user = '', password = '', localhost= True  ):
    '''
    function create connect to mongo db
    :return: 
    '''
    if localhost:
        client = MongoClient('localhost', port )
        db = client[database]
    return db


