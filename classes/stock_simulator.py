import numpy as np
import matplotlib.pyplot as plt

class StockPriceSimulator:
    def __init__(self, S0, T, dt, sigma, Lambda, alpha=1.53):
        """
        Initialize the stock price simulator.

        Parameters:
        S0 (float): Initial stock price.
        T (float): Total time period.
        dt (float): Time step size.
        sigma (float): Standard deviation of the Brownian motion.
        """
        self.S0 = S0        # Initial stock price
        self.T = T          # Total time period
        self.dt = dt        # Time step size
        self.sigma = sigma  # Standard deviation
        self.N = int(T / dt)  # Number of time steps
        self.Lambda = Lambda  # Frequency of orders
        self.alpha = alpha  # Parameter of the distribution of the volume of orders

    def sample_orders(self, x0=1.0, size=1):
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
        U = np.random.uniform(0, 1, size)
        # Inverse transform sampling formula
        x = x0 * (1 - U) ** (-1 / self.alpha)
        # Return single value if size is 1
        return x if size > 1 else x[0]

    def simulate(self):
        """
        Simulate the evolution of the stock price.

        Returns:
        np.ndarray: Array of stock prices at each time step.
        """
        # Generate random increments
        Z = np.random.normal(0, 1, self.N)
        dS = self.sigma * np.sqrt(self.dt) * Z

        # Initialize stock price array
        S = np.zeros(self.N + 1)
        S[0] = self.S0
        S[1:] = self.S0 + np.cumsum(dS)

        # Create vectors for the random number of buy/sell orders
        sell_orders = self.Lambda*self.sample_orders(size=self.N+1)
        buy_orders = self.Lambda*self.sample_orders(size=self.N+1)

        # Define vectors of random price differences according to the logarighmic law
        p_down = S - np.log(sell_orders)
        p_up = S + np.log(buy_orders)
        return S, p_down, p_up
    
    def simulate_and_plot(self):
        '''
        Calls the simulator and plot the results
        '''
        S, p_down, p_up = self.simulate()

        plt.figure(figsize=(10, 6))

        plt.plot(S, label='midprice', color='green')
        plt.plot(p_down, label='p_down', color='red')
        plt.plot(p_up, label='p_up', color='blue')

        # Plot options
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Plot of midprice, p_down, and p_up')
        plt.legend()
        plt.grid(True)
        plt.savefig('figures/stock_simulation.png')
        plt.show()
