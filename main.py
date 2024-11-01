from classes.stock_simulator import StockPriceSimulator
from classes.limit_order_book import LimitOrderBookSimulator

S0 = 100        # Initial stock price
T = 1000         # Total time period
dt = 1        # Time step size
sigma = 0.01*S0  # Standard deviation
N = int(T / dt)  # Number of time steps
Lambda = 10  # Frequency of orders

simulator = LimitOrderBookSimulator(S0, T, dt, sigma, Lambda)
simulator.simulate_and_plot()

# queue of len fixed
# new asks and bids arrive according to Poiusson process