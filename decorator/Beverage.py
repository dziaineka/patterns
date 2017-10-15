class Beverage:
    """base class for different beverages"""

    def __init__(self):
        self._description = 'base of beverage'
        self._cost = 0

    @property
    def cost(self):
        return self._cost

    @property
    def description(self):
        return self._description
