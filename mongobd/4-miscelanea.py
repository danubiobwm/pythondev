from pymongo import MongoClient

#1-Estabelece conexão com o MongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# ERRADO
print(db.laureates.count_documents({
    'prizes':{
        'category': 'physics',
        'share': '1'
    }
}))

#2-Todos laureados que possuem prêmio
# em física e compartilhado
print(db.laureates.count_documents({
    'prizes':{
        '$elemMatch':{
            'category': 'physics',
            'share': '1'
        }
    }
}))

#3-Todos laureados que possuem prêmio em física
# compartilhado antes de 1945
print(db.laureates.count_documents({
    'prizes':{
        '$elemMatch':{
            'category': 'physics',
            'share': '1',
            'year':{'$lt': '1945'}
        }
    }
}))

#4-Utilizando Regex
# Alguns laureados nasceram em lugar
# que se tornaria Polônia

print(db.laureates.distinct(
    'bornCountry',
    {'bornCountry': {'$regex':'Poland'}}
))

# 5-Case insensitive (poland)
print(db.laureates.distinct(
    'bornCountry',
    {'bornCountry': {'$regex':'poland', '$options':"i"}}
))

#6-Utilizando classe Regex
from bson.regex import Regex

print(db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('poland', 'i')}
))

#7-Começa com
print(db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('^Poland')}
))

#8-Termina com \ escape parêntesis
print(db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('now Poland\)$')}
))