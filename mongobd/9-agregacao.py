from pymongo import MongoClient
import timeit

#1-Estabelece conexão com o MongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

cursor = db.laureates.find(
    filter = {'bornCountry': 'USA'},
    projection = {'prizes.year': 1},
    limit = 3
)

for doc in cursor:
    print(doc['prizes'])
    
#2-Refatorando consulta com agregações
print('\n')
cursor = db.laureates.aggregate([
    {'$match': {'bornCountry':'USA'}},
    {'$project': {'prizes.year':1}},
    {'$limit': 3}
])

for doc in cursor:
    print(doc['prizes'])
    
#3-Adicionando novas etapas na agregação
print('\n')
from collections import OrderedDict

print(list(db.laureates.aggregate([
    {'$match': {'bornCountry':'USA'}},
    {'$project': {'prizes.year':1, '_id':0}},
    {'$sort': OrderedDict([('prizes.year', 1)])},
    {'$limit': 3},
    {'$skip': 1}
])))

#4-Quantos laureados nascido nos EUA
print(list(db.laureates.aggregate([
    {'$match': {'bornCountry': 'USA'}},
    {'$count': 'qtd_born_usa'}
])))