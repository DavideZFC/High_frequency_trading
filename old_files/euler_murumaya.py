import numpy as np

def simulate_price_paths(S0, r, sigma, T, steps, N):
    S = np.zeros((N, steps))
    for i in range(N):
        S[i,:] = simulate_price_path(S0, r, sigma, T, steps)
    return S

def simulate_price_path(S0, r, sigma, T, steps):
    deltat = T/steps
    Z = np.random.normal(0,sigma*deltat**0.5,steps)
    S = np.zeros(steps)
    S[0] = S0
    const = (r-sigma**2/2)*deltat

    for i in range(1,steps):
        S[i] = S[i-1]*np.exp(const+Z[i])
    
    return S