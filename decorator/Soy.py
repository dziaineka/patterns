import CondimentDecorator


class Soy(CondimentDecorator.CondimentDecorator):
    """Soy"""

    def __init__(self, beverage):
        super().__init__(beverage)
        self._description = 'Soy (4$)'
        self._cost = 4
