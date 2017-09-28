class Duck:
    """parent class for ducks"""

    def __init__(self, fly_behaviour, quack_behaviour):
        self.__fly_behaviour = fly_behaviour
        self.__quack_behaviour = quack_behaviour
        self._description = 'Master Duck'

    def set_quack_behaviour(self, quack_behaviour):
        self.__quack_behaviour = quack_behaviour

    def set_fly_behaviour(self, fly_behaviour):
        self.__fly_behaviour = fly_behaviour

    def perform_quack(self):
        self.__quack_behaviour()

    def perform_fly(self):
        self.__fly_behaviour()

    def display(self):
        print(self._description)

    def action(self):
        self.display()
        self.perform_fly()
        self.perform_quack()
        print()
