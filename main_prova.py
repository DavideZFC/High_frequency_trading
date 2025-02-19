from classes.market_simulator import MarketSimulator
import matplotlib.pyplot as plt

# buyer, you pay the ask price
# seller, you receive the bid price

mar = MarketSimulator(mu_bid=10.5, mu_ask=11.0, sd=0.25, Lambda=10)

time_horizon = 400
mar.simulate_evolution(horizon=time_horizon, drift=0.001)
plt.plot(mar.midprice_history, label='midprice')
plt.plot(mar.ask_history, label='ask price', color='r', alpha=0.5, linestyle='dashed')
plt.plot(mar.bid_history, label='bid price', color='r', alpha=0.5, linestyle='dashed')
plt.legend()
plt.show()