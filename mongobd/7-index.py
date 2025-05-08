from pymongo import MongoClient
import timeit

#1-Estabelece conexão com o MongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

#1-Busca prêmios de 1910
def get_prizes():
    list(db.prizes.find({'year':'1910'}))
    
#2-Função para medir o tempo de execução
def measure_execution_time(function):
    execution_time = timeit.timeit(function, globals=globals(),
                                   number=1) *1000
    print(f'Tempo de execução:{execution_time:.2f} milissegundos')
    
#3-Sem e com índice
measure_execution_time('get_prizes()')

db.prizes.create_index([('year',1)])
measure_execution_time('get_prizes()')

#4-Criando um índice composto
db.prizes.create_index([('category', 1), ('year',1)])

def get_all_prizes_economics():
    list(db.prizes.find(
        {'category':'economics'},
        {'year':1, '_id':0}
    ))
    
measure_execution_time('get_all_prizes_economics()')