from classes.euler_murumaya import *
import matplotlib.pyplot as plt

S0 = 1
r = -1.0
sigma = 2.0
T = 1
steps = 1000
N = 10
v = simulate_price_paths(S0, r, sigma, T, steps, N)
for i in range(N):
    plt.plot(v[i,:])
plt.show()