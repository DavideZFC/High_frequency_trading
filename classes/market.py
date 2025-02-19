
from classes.limit_order_book import LimitOrderBook
from classes.basics.order import Order

class Market:
    """
    Represents a market with bid and ask limit order books.
    
    Attributes:
        ask_book (LimitOrderBook): The limit order book for ask orders.
        bid_book (LimitOrderBook): The limit order book for bid orders.
    """

    def __init__(self):
        """
        Initializes a Market with separate order books for bids and asks.
        """
        self.ask_book = LimitOrderBook(order_type='ask')
        self.bid_book = LimitOrderBook(order_type='bid')

    def new_order(self, order: Order):
        """
        Processes a new incoming order:
        - Attempts to match it against the opposite book.
        - If there’s remaining size after matching, adds it to the appropriate book.

        Args:
            order (Order): The new incoming order.
        """
        if order.order_type == 'ask':
            # Attempt to match with the bid book; update remaining size
            order.size = self.bid_book.cancel_out(price=order.price, size=order.size)
        else:
            # Attempt to match with the ask book
            order.size = self.ask_book.cancel_out(price=order.price, size=order.size)

        # If part of the order remains unmatched, add it to the appropriate book
        if order.size > 0:
            self.add_order(order)

    def add_order(self, order: Order):
        """
        Adds an order to the correct order book.

        Args:
            order (Order): The order to be added.
        """
        if order.order_type == 'ask':
            self.ask_book.add_order(order)
        else:
            self.bid_book.add_order(order)

    def best_bid_ask(self) -> tuple[float, float]:
        """
        Retrieves the best bid and ask prices from the books.

        Returns:
            tuple[float, float]: Best bid price and best ask price.
        """
        best_bid = self.bid_book.best_price()
        best_ask = self.ask_book.best_price()
        return best_bid, best_ask

    def display_books(self):
        """
        Displays the contents of the bid and ask order books.
        """
        print("Ask Book:")
        self.ask_book.display_orders()
        print("Bid Book:")
        self.bid_book.display_orders()
