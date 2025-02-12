from sortedcontainers import SortedList

class lob:
    def __init__(self, typ):
        self.orders = SortedList()
        self.typ = typ

    def add_order(self, o):
        '''
        adds order in the right place of the queue
        '''
        if not (o.typ == self.typ):
            raise ValueError("wrong order list")


        if (not self.min_value):
            self.min_value = o.value
            self.max_value = o.value
        else:
            self.min_value = min(self.min_value, o.value)
            self.max_value = max(self.max_value, o.value)

        self.orders.add(o)

    def __repr__(self):
        return f"A({self.name}, {self.value})"    
