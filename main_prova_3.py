from classes.market_simulator import MarketSimulator
from classes.policies.standard_market_maker import StandardMarketMaker
import matplotlib.pyplot as plt

# buyer, you pay the ask price
# seller, you receive the bid price

mar = MarketSimulator(mu_bid=10.5, mu_ask=11.0, sd=1.0, Lambda=50)

time_horizon = 1000
name = 'market_making_experiment_{}'.format(time_horizon)
policy = StandardMarketMaker(price_down=10.5, price_up=11.0, size_trade=5)

mar.set_drif(0.00005)
mar.set_horizon(time_horizon)

mar.reset(warmup=10)
for t in range(time_horizon):
    order = policy.trade()
    midprice = mar.step_order(order)
    policy.update(midprice)
    if t % int(time_horizon/10) == 0:
        print(policy.current_amount, policy.money)

print("final revenue:")
print(policy.current_amount, policy.money)

plt.plot(mar.midprice_history, label='midprice')
plt.plot(mar.ask_history, label='ask price', color='g', alpha=0.5, linestyle='dashed')
plt.plot(mar.bid_history, label='bid price', color='r', alpha=0.5, linestyle='dashed')
plt.legend()
plt.savefig('figures/'+name+'.png')
plt.show()