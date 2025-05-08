from pymongo import MongoClient

#1-Estabelece conexão com o MongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

#2-Contar documentos por gênero
print(db.laureates.count_documents({'gender':'female'}))
print(db.laureates.count_documents({'gender':'male'}))

#3-Contar documentos pelo país que morreu
print(db.laureates.count_documents({'diedCountry':'France'}))

#4-Filtro composto com algumas informações
filter_doc = {
    'diedCountry': 'France',
    'gender': 'female',
    'bornCity': 'Warsaw'
}
print(db.laureates.count_documents(filter_doc))
print(db.laureates.find_one(filter_doc))

"""
Marie Curie ganhou pelas descobertas dos elementos radio e polônio
"""

#5-Utilizando o operador in
filter_in = db.laureates.count_documents(
    {
        'diedCountry':{
            '$in':['France', 'USA']
        }
    }
)
print(filter_in)

#6-Utilizando o operador ne - not equal
filter_ne = db.laureates.count_documents({
    'diedCountry':{
        '$ne': 'USA'
    }
})

print(filter_ne)