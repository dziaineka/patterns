from states import state


class CoinInsertedState(state.State):

    def __init__(self, machine):
        super().__init__(machine)

    def turn_crank(self):
        self.machine.set_state(self.machine.gumball_sold_state)
        print('The crank has been turned.')

    @staticmethod
    def insert_coin():
        print('Another coin has already been inserted.')

    def return_coin(self):
        self.machine.set_state(self.machine.no_coin_state)
        print('Coin has been returned.')

    @staticmethod
    def give_ball():
        print('You have to turn crank.')


