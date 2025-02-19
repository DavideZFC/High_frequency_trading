
from classes.basics.order import Order
from classes.market import Market
import numpy as np


class MarketSimulator:
    """
    Simulates the evolution of a limit order book with randomly generated orders.

    Attributes:
        market (Market): The simulated market containing bid and ask books.
        order_id (int): Counter for generating unique order IDs.
        mu_bid (float): Mean bid price for generating random orders.
        mu_ask (float): Mean ask price for generating random orders.
        sd (float): Standard deviation for price generation.
        Lambda (int): Frequency of order generation per time step.
        alpha (float): Parameter for order size distribution.
    """

    def __init__(self, mu_bid: float, mu_ask: float, sd: float, Lambda: int = 10, alpha: float = 1.53):
        """
        Initializes the MarketSimulator.

        Args:
            mu_bid (float): Mean bid price.
            mu_ask (float): Mean ask price.
            sd (float): Standard deviation for price generation.
            Lambda (int, optional): Number of orders generated per time step. Defaults to 10.
            alpha (float, optional): Power-law exponent for order size distribution. Defaults to 1.53.
        """
        self.market = Market()
        self.order_id = 0
        self.mu_bid = mu_bid
        self.mu_ask = mu_ask
        self.sd = sd
        self.Lambda = Lambda
        self.alpha = alpha

    def get_random_order(self, order_type: str):
        """
        Generates a random order with price sampled from a normal distribution and size from a power-law distribution.

        Args:
            order_type (str): 'bid' or 'ask'.

        Returns:
            Order: Randomly generated order.
        """
        mu = self.mu_bid if order_type == 'bid' else self.mu_ask
        price = np.random.normal(mu, self.sd)
        size = self.sample_order_size()
        order = Order(str(self.order_id), price, order_type, size)
        self.order_id += 1
        return order

    def sample_order_size(self, x0: float = 1.0):
        """
        Samples an order size from a power-law distribution using inverse transform sampling.

        Args:
            x0 (float, optional): Lower bound for the size. Defaults to 1.0.

        Returns:
            int: Sampled order size.
        """
        U = np.random.uniform(0, 1)
        size = x0 * (1 - U) ** (-1 / self.alpha)
        return max(1, int(size))  # Ensure size is at least 1

    def simulate_evolution(self, horizon: int, drift: float = 0, p: float = 0.5):
        """
        Simulates the market evolution over a specified time horizon.

        Args:
            horizon (int): Number of time steps to simulate.
            drift (float, optional): Increment added to mu_bid and mu_ask at each step. Defaults to 0.
            p (float, optional): Probability of generating a 'bid' order (1-p for 'ask'). Defaults to 0.5.
        """
        self.midprice_history = np.zeros(horizon)
        self.ask_history = np.zeros(horizon)
        self.bid_history = np.zeros(horizon)

        for t in range(horizon):
            # Generate Lambda random orders at each time step
            for _ in range(self.Lambda):
                order_type = 'ask' if np.random.binomial(1, p) == 0 else 'bid'
                order = self.get_random_order(order_type)
                self.market.new_order(order)

            # Retrieve best bid and ask prices
            bid, ask = self.market.best_bid_ask()

            # Compute and store midprice and best prices, ensuring realistic bounds
            midprice = (bid + ask) / 2
            self.midprice_history[t] = np.clip(midprice, self.mu_bid / 2, self.mu_ask * 2)
            self.ask_history[t] = np.clip(ask, self.mu_bid / 2, self.mu_ask * 2)
            self.bid_history[t] = np.clip(bid, self.mu_bid / 2, self.mu_ask * 2)

            # Apply drift to move the price means over time
            self.mu_bid += drift
            self.mu_ask += drift
