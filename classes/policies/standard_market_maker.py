from classes.basics.order import Order


class StandardMarketMaker:
    def __init__(self, price_up, price_down, size_trade=5, initial_amount=0, money=0, time_horizon=1000):
        self.price_up = price_up
        self.price_down = price_down
        self.current_amount = initial_amount
        self.money = money
        self.time_horizon = time_horizon
        self.t = 0
        self.size_trade = size_trade

    def callback(self, size, price, order_type):
        if order_type == "ask":
            self.money += size*price
        elif order_type == "bid":
            self.money -= size*price
            self.current_amount += size

    def trade(self):
        id = "my_order_"+str(self.t)
        self.t += 1
        if self.t % 2 == 0:
            return Order(id, self.price_down, "bid", self.size_trade, self.callback)
        if self.t % 2 == 1:
            size = min(self.size_trade, self.current_amount)
            self.current_amount -= size
            return Order(id, self.price_up, "ask", size, self.callback)
        
    def update(self, midprice):
        pass