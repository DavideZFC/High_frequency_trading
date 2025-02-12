
class order:
    def __init__(self, id, value, typ):
        '''
        id : order id (str)
        value : order value (double)
        typ: bid or ask (str)
        '''
        self.id = id
        self.value = value
        self.typ = typ

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"order({self.id}, {self.value}, {self.typ})"