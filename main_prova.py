from sortedcontainers import SortedList

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
