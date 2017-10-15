import CondimentDecorator


class Milk(CondimentDecorator.CondimentDecorator):
    """Milk"""

    def __init__(self, beverage):
        super().__init__(beverage)
        self._description = 'Milk (6$)'
        self._cost = 6
