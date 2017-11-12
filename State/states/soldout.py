from states import state


class SoldOut(state.State):
    def __init__(self, machine):
        super().__init__(machine)

    @staticmethod
    def turn_crank():
        print('There are no gumballs in the machine.')

    @staticmethod
    def insert_coin():
        print('There are no gumballs in the machine.')

    @staticmethod
    def return_coin():
        print('There are no coins in the machine.')

    def refill(self, amount):
        super().refill(amount)
        self.machine.set_state(self.machine.no_coin_state)

    @staticmethod
    def give_ball():
        print('There are no balls.')


