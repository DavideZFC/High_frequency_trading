# 📈 Limit Order Book Simulator

Welcome to the **Limit Order Book Simulator**! 🚀 This project models a financial market where bid and ask orders compete for liquidity. If you've ever wondered how stock exchanges match buyers and sellers, you're in the right place! 🏦💸

## 🧩 Project Structure

- **Order**: Represents individual buy/sell orders with price, size, and type.
- **LimitOrderBook**: Manages bids and asks in a sorted order book.
- **Market**: Facilitates order matching and keeps track of the best prices.
- **MarketSimulator**: Generates random orders and simulates market evolution over time.

## 🔥 Features

✅ Realistic order generation with Gaussian price distribution and power-law size distribution.\
✅ Simulates market evolution with customizable drift and order frequency.\
✅ Tracks midprice, bid, and ask prices over a specified time horizon.\
✅ Fully commented, clean, and readable code (yes, even your future self will thank you).

## 🚀 Quick Start

```python
from classes.market_simulator import MarketSimulator

# Initialize simulator with mean bid/ask prices, price volatility, order frequency, and size distribution parameter
sim = MarketSimulator(mu_bid=99, mu_ask=101, sd=1, Lambda=20, alpha=1.5)

# Run simulation for 100 time steps with a small drift towards higher prices
sim.simulate_evolution(horizon=100, drift=0.01, p=0.5)

# Access midprice history
print(sim.midprice_history)
```

## 📊 Example Output (Midprice Evolution)

```
[100.0, 100.2, 100.5, 100.9, 101.3, ...]
```

*Midprice steadily drifts upward thanks to the positive drift parameter.* 📈

## 🎯 Why This Project?

This simulator is a great starting point for:

- Studying market microstructure 🔍
- Backtesting trading strategies 🧠
- Understanding order flow and price formation 🏛️

## 🤓 Author Notes

- Code follows PEP 8 standards 🐍.
- Comments and docstrings are here to **help, not confuse**. 😎
- Built with love ❤️ and too much coffee ☕.

## 🚀 Future Ideas

- Market impact modeling 🏗️
- Real-time visualizations 📺
- Integration with real market data 🌍

---

💡 *"Markets can remain irrational longer than you can remain solvent."* — John Maynard Keynes 💸

