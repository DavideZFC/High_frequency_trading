

class MovingAverageCrossover:
    def __init__(self, initial_amount=0, money=0, short_window=10, long_window=30, size_trade=10):
        """
        Inizializza lo stratega del Moving Average Crossover.

        Args:
            initial_amount (int): Numero iniziale di azioni in portafoglio.
            money (float): Liquidità iniziale.
            short_window (int): Finestra per la media mobile breve.
            long_window (int): Finestra per la media mobile lunga.
        """
        self.current_amount = initial_amount
        self.money = money
        self.short_window = short_window
        self.long_window = long_window
        self.prices = [] 
        self.current_signal = "hold"
        self.size_trade = size_trade

    def update(self, action, price, revenue, remaining):
        """
        Update agent parameters depending on the result of the trade

        Args:
            action (tuple): string (sell/buy) and int corresponding to the size
            price (float): new midprice of the stock
            remaining (int): amount that we could not sell or buy
            revenue (float): how much money we made
        """
        # update our current amount
        if action[0] == "sell":
            self.current_amount = self.current_amount - action[1] + remaining
        else:
            self.current_amount = self.current_amount + action[1] - remaining

        self.money -= revenue
        self.observe_price(price)

    def observe_price(self, price):
        """
        Aggiorna la cronologia dei prezzi e ricalcola le medie mobili per generare un segnale.

        Args:
            price (float): Prezzo corrente dell'asset.
        """
        self.prices.append(price)

        if len(self.prices) >= self.long_window:
            short_ma = sum(self.prices[-self.short_window:]) / self.short_window
            long_ma = sum(self.prices[-self.long_window:]) / self.long_window

            if short_ma > long_ma:
                self.current_signal = "buy"
            elif short_ma < long_ma:
                self.current_signal = "sell"
            else:
                self.current_signal = "hold"
        else:
            # not enough data, keep "hold"
            self.current_signal = "hold"

    def trade(self):
        # we have to take into account that if we buy immediately a big quantity of a given stock, 
        # the price could be much different than the midprice, depending on the depth of the order book

        if self.current_signal == "hold":
            # holding corresponds to buying zero
            return "buy", 0

        if self.current_signal == "sell":
            # we cannot sell more than what we have
            size_trade = min(self.size_trade, self.current_amount)
            return self.current_signal, size_trade

        return self.current_signal, self.size_trade
