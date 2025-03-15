from classes.market_simulator import MarketSimulator
import matplotlib.pyplot as plt
from classes.basics.order import Order

# buyer, you pay the ask price
# seller, you receive the bid price

mar = MarketSimulator(mu_bid=10.5, mu_ask=11.0, sd=1.0, Lambda=5)

time_horizon = 200
name = 'price_variation_hor_{}'.format(time_horizon)

mar.market.add_order(Order('1', 10, 'bid', 100))
mar.market.add_order(Order('3', 11, 'bid', 1000))
mar.market.add_order(Order('2', 12, 'ask', 100))
mar.market.add_order(Order('4', 13, 'ask', 10))

mar.market.display_books()
print(mar.market.operate_now(20, 'buy'))
mar.market.display_books()