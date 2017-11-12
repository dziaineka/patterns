from states import state


class GumballSoldState(state.State):
    def __init__(self, machine):
        super().__init__(machine)

    @staticmethod
    def turn_crank():
        print('Ball giving in progress.')

    @staticmethod
    def insert_coin():
        print('You should to receive previous gumball.')

    @staticmethod
    def return_coin():
        print('Too late.')

    def give_ball(self):
        self.machine.amount -= 1

        if self.machine.amount > 0:
            self.machine.set_state(self.machine.no_coin_state)
        else:
            self.machine.set_state(self.machine.soldout)

        print('One ball has been sold.')
