from classes.limit_order_book_V2 import lob

class market:

    def __init__(self):
        self.ask_book = lob(typ = 'ask')
        self.bid_book = lob(typ = 'bid')

    def add_order(self, o):
        '''
        adds order o to the right queue
        '''
        if o.typ == 'ask':
            self.ask_book.add_order(o)
        else:
            self.bid_book.add_order(o)

    def print(self):
        self.ask_book.print()
        self.bid_book.print()     