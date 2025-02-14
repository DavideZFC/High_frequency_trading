from classes.market_simulator import market_simularor


# buyer, you pay the ask price
# seller, you receive the bid price

mar = market_simularor(mu_bid=0.5, mu_ask=1.0, sd=1)

time_horizon = 100
for i in range(time_horizon):
    if i % 2 == 0:
        typ = 'ask'
    else:
        typ = 'bid'
    mar.add_random_order(typ)
