from classes.market_simulator import market_simularor
import matplotlib.pyplot as plt

# buyer, you pay the ask price
# seller, you receive the bid price

mar = market_simularor(mu_bid=0.5, mu_ask=1.0, sd=0.25, Lambda=10)

time_horizon = 400
mar.simulate_evolution(horizon=time_horizon, drift=0.001)
plt.plot(mar.midprice_history, label='midprice')
plt.plot(mar.ask_history, label='ask price')
plt.plot(mar.bid_history, label='bid price')
plt.legend()
plt.show()