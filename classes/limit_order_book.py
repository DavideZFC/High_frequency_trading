import numpy as np
import matplotlib.pyplot as plt

class LimitOrderBookSimulator:
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
        self.bids = np.array([]) # vector of the bids
        self.asks = np.array([]) # vector of the ask

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
    
    def simplify(self):
        '''
        Simplify ask and bids so that the vectors remain disjoint
        '''
        m = min(len(self.asks), len(self.bids))
        i = 0

        while i < m:
            if self.bids[-i-1] > self.asks[i]:
                i += 1
            else:
                break
        
        if i>0:
            self.bids = self.bids[:-i]
            self.asks = self.asks[i:]
            print('{} selling completed'.format(i))


    def simulate(self):
        """
        Simulate the evolution of the stock price.

        Returns:
        np.ndarray: Array of stock prices at each time step.
        """

        # Initialize stock price array
        S = np.zeros(self.N + 1)
        S[0] = self.S0

        # Initialize queue length
        queue_len = np.zeros(self.N + 1)
        queue_len[0] = 0

        # Create vectors for the random number of buy/sell orders
        sell_orders = self.Lambda*self.sample_orders(size=self.N+1)
        buy_orders = self.Lambda*self.sample_orders(size=self.N+1)

        for i in range(self.N):
            # Compute delta_bid values
            delta_bids = np.random.exponential(size=int(sell_orders[i]))
            delta_asks = np.random.exponential(size=int(buy_orders[i]))
            shift = np.random.normal(0,self.sigma)

            # Center the order w.r.t. the mean
            new_bids = S[i] - delta_bids + shift
            new_asks = S[i] + delta_asks + shift

            self.bids = np.sort(np.append(self.bids, new_bids))
            self.asks = np.sort(np.append(self.asks, new_asks))

            self.simplify()
            S[i+1] = (self.bids[-1] + self.asks[0])/2
            queue_len[i+1] = len(self.bids) + len(self.asks)

        return S, queue_len

    def simulate_and_plot(self):
        '''
        Calls the simulator and plot the results
        '''
        S, queue_len = self.simulate()

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 7))

        # Plot on the first subfigure
        ax1.plot(S, label='midprice', color='green')

        # Plot options
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Value')
        ax1.set_title('Plot of midprice')

        # Plot on the second subfigure
        ax2.plot(queue_len, label='queue_len', color='C0')

        # Plot options
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Length')
        ax2.set_title('Len of the queue (sum of ask and bid)')

        plt.tight_layout()  # Adjust layout to prevent overlap
        plt.savefig('figures/limit_order_simulation.png')
        plt.show()
