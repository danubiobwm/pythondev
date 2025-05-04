from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
mydb = client.dbpost
mycol = mydb.posts

post1 = {
    "author": "John Doe",
    "text": "This is a post",
    "tags": ["mongodb", "python", "pymongo"],
    "date": "2023-10-01",
    "likes": 10,
    "comments": [
        {"author": "Jane Doe", "text": "Great post!", "date": "2023-10-02"},
        {"author": "Alice", "text": "Thanks for sharing!", "date": "2023-10-03"}
    ]
}

post2 = {
    "author": "Alice",
    "text": "Another post",
    "tags": ["mongodb", "python"],
    "date": "2023-10-04",
    "likes": 5,
    "comments": [
        {"author": "Bob", "text": "Interesting!", "date": "2023-10-05"}
    ]
}

result = mycol.insert_one(post1)
print("Post 1 inserted with id:", result.inserted_id)

result = mycol.insert_one(post2)
print("Post 2 inserted with id:", result.inserted_id)
