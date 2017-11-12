from states import state


class NoCoin(state.State):
    def __init__(self, machine):
        super().__init__(machine)

    @staticmethod
    def turn_crank():
        print('There is no coin in the machine.')

    def insert_coin(self):
        self.machine.set_state(self.machine.coin_inserted_state)
        print('Coin has been inserted.')

    @staticmethod
    def return_coin():
        print('There are no coins in the machine.')

    @staticmethod
    def give_ball():
        print('You have to input coin first.')
