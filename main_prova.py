from classes.market import market
from classes.basics.order import order


# buyer, you pay the ask price
# seller, you receive the bid price

mar = market()

o = order(id='1', value=10, typ='bid')
mar.new_order(o)
o = order(id='2', value=11, typ='bid')
mar.new_order(o)
o = order(id='3', value=4, typ='ask')
mar.new_order(o)
o = order(id='4', value=7, typ='ask')
mar.new_order(o)
print(mar.ask_book.get_first())
print(mar.bid_book.get_first())

'''
class A:
    def __init__(self, name, value):
        self.name = name
        self.value = value  # Questo sarà usato per l'ordinamento

    def __lt__(self, other):
        return self.value < other.value  # Ordinamento basato su `value`

    def __repr__(self):
        return f"A({self.name}, {self.value})"

# Creazione della SortedList
sl = SortedList()

print(A("apple", 10) < A("apple", 2))

# Aggiunta di elementi
sl.add(A("apple", 10))
sl.add(A("banana", 5))
sl.add(A("cherry", 20))

print(sl)  # Output: [A(banana, 5), A(apple, 10), A(cherry, 20)]

# Rimozione del primo elemento (minimo)
print(sl.pop(0))  # Output: A(banana, 5)
'''