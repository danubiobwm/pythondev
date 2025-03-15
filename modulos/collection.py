from collections import Counter, namedtuple, deque
from operator import itemgetter

fruits = ["maça", "banana", "uva", "pera", "banana", "maça", "banana", "uva", "pera", "banana", "maça", "Abacaxi", "Tangerina", "pera", "banana"]

print(fruits)
print(Counter(fruits))

game = namedtuple("game", ["name", "price", "note"])
g1 = game("Fifa 23", 90.5, 8.5)
g2 = game("Fifa 25", 50.5, 6.5)
print(g1)
print(g2)

