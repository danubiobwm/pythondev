from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
mydb = client.dbpost
mycol = mydb.posts

#delete a single document
# {'_id': ObjectId('6817e95104917bc223b435f3'),
#  'author': 'John Doe',

delete_query = {"_id": ObjectId("6817e95104917bc223b435f3")}
#  'comments': [{'author': 'Jane Doe',
mycol.delete_one(delete_query)
print("Deleted document with _id 6817e95104917bc223b435f3")

