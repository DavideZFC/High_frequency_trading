

class MovingAverageCrossover:
    def __init__(self, size, money, short_window=10, long_window=30, size_trade=10):
        """
        Inizializza lo stratega del Moving Average Crossover.

        Args:
            size (int): Numero iniziale di azioni in portafoglio.
            money (float): Liquidità iniziale.
            short_window (int): Finestra per la media mobile breve.
            long_window (int): Finestra per la media mobile lunga.
        """
        self.size = size
        self.money = money
        self.short_window = short_window
        self.long_window = long_window
        self.prices = [] 
        self.current_signal = "hold"
        self.size_trade = size_trade

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
        return self.current_signal, self.size
