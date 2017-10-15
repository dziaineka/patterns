import CondimentDecorator


class Mocha(CondimentDecorator.CondimentDecorator):
    """Mocha"""

    def __init__(self, beverage):
        super().__init__(beverage)
        self._description = 'Mocha (5$)'
        self._cost = 5
