from classes.limit_order_book_V2 import lob

class market:

    def __init__(self):
        self.ask_book = lob(typ = 'ask')
        self.bid_book = lob(typ = 'bid')


    def new_order(self, o):
        if o.typ == 'ask':
            o.size = self.bid_book.cancel_out(o.value, o.size)
            # modifying size erasing what is sold
        else:
            o.size = self.ask_book.cancel_out(o.value, o.size)
        if o.size > 0:
            self.add_order(o)


    def add_order(self, o):
        '''
        adds order o to the right queue
        '''
        if o.typ == 'ask':
            self.ask_book.add_order(o)
        else:
            self.bid_book.add_order(o)


    def best_difference(self):
        bid = self.bid_book.best_price()
        ask = self.ask_book.best_price()
        return (bid, ask)


    def print(self):
        self.ask_book.print()
        self.bid_book.print()     