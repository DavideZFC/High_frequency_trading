from classes.basics.order import order
from classes.market import market
import numpy as np


class market_simularor:
    def __init__(self, mu_bid, mu_ask, sd):
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
    
    def add_random_order(self, typ):
        '''
        adds a random order with specified parameters
        '''
        mu = self.mu_bid if typ == 'bid' else self.mu_ask
        value = np.random.normal(mu, self.sd)

        o = order(str(self.order_id), value, typ)
        self.mark.new_order(o)

        self.order_id += 1