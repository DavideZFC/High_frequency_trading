
from sortedcontainers import SortedList

class LimitOrderBook:
    """
    Represents a Limit Order Book (LOB) for either bids or asks.

    Attributes:
        order_type (str): Type of the book, either 'bid' or 'ask'.
        orders (SortedList): Sorted list of orders.
    """

    def __init__(self, order_type: str):
        """
        Initializes a Limit Order Book for a specific order type.

        Args:
            order_type (str): 'bid' or 'ask'.

        Raises:
            ValueError: If order_type is not 'bid' or 'ask'.
        """
        if order_type not in {'bid', 'ask'}:
            raise ValueError("order_type must be 'bid' or 'ask'")
        self.orders = SortedList()
        self.order_type = order_type

    def add_order(self, order):
        """
        Adds an order to the book in the correct position.

        Args:
            order (Order): The order to be added.

        Raises:
            ValueError: If the order's type doesn't match the book type.
        """
        if order.order_type != self.order_type:
            raise ValueError(
                f"Order type mismatch: book type = '{self.order_type}', order type = '{order.order_type}'"
            )
        self.orders.add(order)

    def get_first(self):
        """
        Retrieves and removes the best order (highest bid or lowest ask).

        Returns:
            Order | None: The best order or None if the book is empty.
        """
        return self.orders.pop(0) if self.orders else None

    def best_price(self):
        """
        Gets the best price in the order book.

        Returns:
            float: Best price or ±infinity if the book is empty.
        """
        if self.orders:
            return self.orders[0].price
        return float('inf') if self.order_type == 'ask' else float('-inf')

    def cancel_out(self, price: float, size: int):
        """
        Matches incoming market orders against the order book until the size is filled or no match is possible.

        Args:
            price (float): Price of the incoming order.
            size (int): Size of the incoming order.

        Returns:
            int: Remaining size after matching.

        Note:
            - For 'ask' books, orders with price ≥ best ask are matched.
            - For 'bid' books, orders with price ≤ best bid are matched.
        """
        while self.orders:
            best_price = self.best_price()
            # Check if the incoming order price can match with the best order
            if (self.order_type == 'ask' and price > best_price) or (self.order_type == 'bid' and price < best_price):
                top_order = self.orders[0]
                
                if size >= top_order.size:
                    # Fully consume the top order
                    size -= top_order.size
                    self.get_first()
                else:
                    # Partially consume the top order
                    top_order.size -= size
                    return 0
            else:
                break
        return size

    def display_orders(self):
        """
        Prints all orders in the order book for debugging purposes.
        """
        print(self.orders)
