from old_files.order import order
from old_files.market import market
import numpy as np


class market_simularor:
    def __init__(self, mu_bid, mu_ask, sd, Lambda=10, alpha=1.53):
        '''
        Generates random orders to put in a market: 
        the orders are generated with mean mu_bid / mu_ask and fixed standard deviation
        according to a Gaussian distribution
        '''

        self.mark = market()
        self.order_id = 0
        self.mu_bid = mu_bid
        self.mu_ask = mu_ask
        self.sd = sd

        self.Lambda = Lambda  # Frequency of orders (number per day)
        self.alpha = alpha  # Parameter of the distribution of the volume of orders (alternative value: 1.4)

    
    def get_random_order(self, typ):
        '''
        creates a random order with specified parameters
        '''
        mu = self.mu_bid if typ == 'bid' else self.mu_ask
        value = np.random.normal(mu, self.sd)

        o = order(str(self.order_id), value, typ, size=self.sample_order_size())
        self.order_id += 1
        return o


    def sample_order_size(self, x0=1.0):
        """
        Sample from a density function proportional to x^(-1 - a).

        Parameters:
        a (float): Positive parameter of the density function.
        x0 (float): Lower bound of x (x ≥ x0). Default is 1.0.
        size (int): Number of samples to generate. Default is 1.

        Returns:
        numpy.ndarray or float: Sample(s) drawn from the distribution.
        """

        # Generate uniform random numbers between 0 and 1
        U = np.random.uniform(0, 1)
        # Inverse transform sampling formula
        size = x0 * (1 - U) ** (-1 / self.alpha)

        return int(size)
    

    def simulate_evolution(self, horizon, drift=0, p=0.5):

        # here we store the sequence of midprices
        self.midprice_history = np.zeros(horizon)
        self.ask_history = np.zeros(horizon)
        self.bid_history = np.zeros(horizon)
        
        for t in range(horizon):

            for j in range(self.Lambda):

                typ = 'ask' if np.random.binomial(1,p) == 0 else 'bid'

                o = self.get_random_order(typ)
                self.mark.new_order(o)
            
            # update means according to the drift
            bid, ask = self.mark.best_difference()
            self.midprice_history[t] = np.clip((bid + ask)/2, self.mu_bid/2, self.mu_ask*2)
            self.ask_history[t] = np.clip(ask, self.mu_bid/2, self.mu_ask*2)
            self.bid_history[t] = np.clip(bid, self.mu_bid/2, self.mu_ask*2)

            self.mu_bid += drift
            self.mu_ask += drift

