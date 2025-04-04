from classes.market_simulator import MarketSimulator
from classes.policies.moving_average_crossover import MovingAverageCrossover
import matplotlib.pyplot as plt

# buyer, you pay the ask price
# seller, you receive the bid price

mar = MarketSimulator(mu_bid=10.5, mu_ask=11.0, sd=1.0, Lambda=50)

time_horizon = 20
name = 'price_variation_hor_{}'.format(time_horizon)
policy = MovingAverageCrossover(short_window=20, long_window=50, size_trade=5, time_horizon=time_horizon)

mar.set_drif(0.0005)
mar.set_horizon(time_horizon)

mar.reset(warmup=10)
for t in range(time_horizon):
    action = policy.trade()
    midprice, revenue, remaining = mar.step(action)
    policy.update(action, midprice, revenue, remaining)
    if t % 100 == 0:
        print(policy.current_amount, policy.money)

print("final revenue:")
print(policy.current_amount, policy.money)

plt.plot(mar.midprice_history, label='midprice')
plt.plot(mar.ask_history, label='ask price', color='g', alpha=0.5, linestyle='dashed')
plt.plot(mar.bid_history, label='bid price', color='r', alpha=0.5, linestyle='dashed')
plt.legend()
plt.savefig('figures/'+name+'.png')
plt.show()