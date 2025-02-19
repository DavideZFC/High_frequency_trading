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
        return self.orders.pop(0)
    
    def best_price(self):
        if len(self.orders) > 0:
            return self.orders[0].value
        if self.typ == 'ask':
            return 100000
        return -100000
    
    def cancel_out(self, value, size):
        while True:
            if (self.typ == 'ask' and value > self.best_price()) or (self.typ == 'bid' and value < self.best_price()):
                if size > self.orders[0].size:
                    o1 = self.get_first()
                    size -= o1.size
                else:
                    self.orders[0].size -= size
                    return 0
            else: 
                break
        return size


    def print(self):
        print(self.orders)
