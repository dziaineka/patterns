from states import gumballsold, nocoin, soldout, coininserted


class GumballMachine:
    def __init__(self, amount):
        self.amount = amount

        # Machine states
        self.gumball_sold_state = gumballsold.GumballSoldState(self)
        self.no_coin_state = nocoin.NoCoin(self)
        self.coin_inserted_state = coininserted.CoinInsertedState(self)
        self.soldout = soldout.SoldOut(self)

        if self.amount > 0:
            self.state = self.no_coin_state
        else:
            self.state = self.soldout

    def set_state(self, state):
        self.state = state

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def refill(self, amount):
        self.state.refill(amount)

    def turn_crank(self):
        self.state.turn_crank()
        self.state.give_ball()

    def insert_coin(self):
        self.state.insert_coin()

    def return_coin(self):
        self.state.return_coin()
