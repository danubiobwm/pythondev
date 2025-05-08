from pymongo import MongoClient
import timeit

#1-Estabelece conexão com o MongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

#1-Todos os prêmios compartilhados entre 3 pessoas
for doc in db.prizes.find({
    'laureates.share': '3'
}):
    print('{year} {category}'.format(**doc))

print('\n')

#2-Utilizando o Limit
for doc in db.prizes.find({
    'laureates.share': '3'
}, limit=5):
    print('{year} {category}'.format(**doc))

print('\n')

#3-Utilizando o Skip
for doc in db.prizes.find({
    'laureates.share': '3'
}, skip=5, limit=5): #Pulando os 5 primeiros resultados
    print('{year} {category}'.format(**doc))

print('\n')

#4-Refatorando | Ordenando ascendentemente
for doc in db.prizes.find({'laureates.share':'3'}) \
    .sort([('year', 1)]) \
    .skip(3) \
    .limit(3):
        print('{year} {category}'.format(**doc))