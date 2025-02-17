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
        print(f'new order of type {o.typ} added')

        '''
        if o.typ == 'ask':
            if self.bid_book.best_price() > o.value:
                o1 = self.bid_book.get_first()
                print(f'transition occured at value {o1.value}')
                return
        if o.typ == 'bid':
            if self.ask_book.best_price() < o.value:
                o1 = self.ask_book.get_first()
                print(f'transition occured at value {o1.value}')
                return
        self.add_order(o)
        print(f'new order of type {o.typ} added')
        '''

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