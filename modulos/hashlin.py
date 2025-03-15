from email import message
import hashlib

#verificar os algoritmos disponiveis
print(hashlib.algorithms_available)

#verificar os algoritmos de acordo com SO
print(hashlib.algorithms_guaranteed)


#Usando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = 'A melhor de prever o futuro é criá-lo'.encode()
algorithm.update(message)
print(algorithm.hexdigest())

#Utilizando o md5
print('#Utilizando o md5')
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
