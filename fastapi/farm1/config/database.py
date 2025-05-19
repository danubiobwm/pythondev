from pymongo import MongoClient

MongoClient = MongoClient("mongodb://localhost:27017/")
db = MongoClient["db_play"]