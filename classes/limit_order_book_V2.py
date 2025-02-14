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
        if len(self.orders) == 0:
            return None
        if self.typ == 'ask':
            return self.orders.pop(0)
        return self.orders.pop()
    
    def best_price(self):
        if len(self.orders) > 0:
            if self.typ == 'ask':
                return self.orders[0].value
            else:
                return self.orders[-1].value
        if self.typ == 'ask':
            return 100000
        return -100000

    def print(self):
        print(self.orders)
