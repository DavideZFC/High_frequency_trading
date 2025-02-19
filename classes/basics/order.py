
class Order:
    """
    Represents an order in the limit order book.

    Attributes:
        id (str): Unique identifier for the order.
        price (float): Price of the order.
        order_type (str): Type of order, either 'bid' or 'ask'.
        size (int): Size or quantity of the order. Defaults to 1.
    """

    def __init__(self, id: str, price: float, order_type: str, size: int = 1):
        if order_type not in {'bid', 'ask'}:
            raise ValueError("order_type must be 'bid' or 'ask'")
        if price <= 0:
            raise ValueError("price must be positive")

        self.id = id
        self.price = price
        self.order_type = order_type
        self.size = size

    def __lt__(self, other: "Order") -> bool:
        """
        Compare orders based on price and type.

        For 'ask' orders: lower price has higher priority.  
        For 'bid' orders: higher price has higher priority.

        Args:
            other (Order): Another order to compare against.

        Returns:
            bool: True if self is less than other based on priority rules.
        """
        if self.order_type == 'ask':
            return self.price < other.price
        return self.price > other.price  # For 'bid'

    def __repr__(self) -> str:
        return f"Order(id='{self.id}', price={self.price}, order_type='{self.order_type}', size={self.size})"
