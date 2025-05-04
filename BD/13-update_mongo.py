from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
mydb = client.dbpost
mycol = mydb.posts

# Update a single document
# {'_id': ObjectId('6817e95104917bc223b435f3'),
#  'author': 'John Doe',
#  'comments': [{'author': 'Jane Doe',
#                'date': '2023-10-02',
#                'text': 'Great post!'},
#               {'author': 'Alice',
#                'date': '2023-10-03',
#                'text': 'Thanks for sharing!'}],
#  'date': '2023-10-01',
#  'likes': 10,
#  'tags': ['mongodb', 'python', 'pymongo'],
#  'text': 'This is a post'}

myquery = {"_id": ObjectId("6817e95104917bc223b435f3")}
newvalues = {"$set": {"author": "John Smith"}}
mycol.update_one(myquery, newvalues)
print("Updated author to John Smith")