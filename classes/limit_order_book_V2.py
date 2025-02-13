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
            raise ValueError("wrong order book: book type = {}, order type = {}".format(self.typ, o.typ))

        self.orders.add(o)

    def get_first(self):
        if self.typ == 'ask':
            return self.orders.pop(0)
        return self.orders.pop()

    def print(self):
        print(self.orders)
