from pymongo import MongoClient

#1-Estabelece conexão com o MongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

#1-valor incluído
#0-valor não incluído

docs = db.laureates.find(
    filter = {},
    projection = {
        'prizes.affiliations': 1,
        '_id':0
    }
)
print(docs)
print(list(docs[:3]))

#2-Projeção com campos ausentes
docs_2 = db.laureates.find(
    filter = {'gender': 'org'},
    projection = ['0', 'firstname']
)
print('\n')
print(list(docs_2[:3]))