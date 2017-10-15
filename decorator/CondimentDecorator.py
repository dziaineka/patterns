import Beverage


class CondimentDecorator(Beverage.Beverage):
    """CondimentDecorator"""

    def __init__(self, beverage):
        self._description = 'Condiment'
        self._cost = 0
        self.beverage = beverage

    @property
    def cost(self):
        return self.beverage.cost + self._cost

    @property
    def description(self):
        return self.beverage.description + ' + ' + self._description
