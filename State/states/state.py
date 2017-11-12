class State(object):

    def __init__(self, machine):
        self.machine = machine

    def refill(self, amount):
        self.machine.set_amount(self.machine.get_amount() + amount)
        print('Gumball machine has been refilled with {} gumballs.'
              .format(amount))


