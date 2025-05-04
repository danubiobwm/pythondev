from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
mydb = client.dbpost
mycol = mydb.posts

# List all posts in the collection
posts = mycol.find()

for post in posts:
  pprint(post)
