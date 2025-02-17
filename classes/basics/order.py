
class order:
    def __init__(self, id, value, typ, size=1):
        '''
        id : order id (str)
        value : order value (double)
        typ: bid or ask (str)
        '''
        self.id = id
        self.value = value
        self.typ = typ
        self.size = size

    def __lt__(self, other):
        if self.typ == 'ask':
            return self.value < other.value
        else:
            return self.value > other.value

    def __repr__(self):
        return f"order({self.id}, {self.value}, {self.typ}, {self.size})"