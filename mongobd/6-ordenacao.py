from pymongo import MongoClient

#1-Estabelece conexão com o MongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

#2-Ordenação Ascendente
cursor = db.prizes.find(
    {'category': 'physics'},
    ['year'],
    sort=[('year', 1)]
)

print([doc['year'] for doc in cursor][:5])

#3-Ordenação Descendente
cursor_2 = db.prizes.find(
    {'category': 'physics'},
    ['year'],
    sort=[('year', -1)]
)

print([doc['year'] for doc in cursor_2][:5])

#4-Prêmios concedidos entre 1966 e 1970
for doc in db.prizes.find(
    {'year':{'$gt':'1966', '$lt':'1970'}},
    ['category', 'year'],
    sort=[('year', 1), ('category', -1)]):
    print('{year} {category}'.format(**doc))