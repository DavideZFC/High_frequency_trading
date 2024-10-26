from classes.stock_simulator import StockPriceSimulator

S0 = 100        # Initial stock price
T = 1000         # Total time period
dt = 1        # Time step size
sigma = 0.1  # Standard deviation
N = int(T / dt)  # Number of time steps
Lambda = 30  # Frequency of orders

simulator = StockPriceSimulator(S0, T, dt, sigma, Lambda)
simulator.simulate_and_plot()