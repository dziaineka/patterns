import Beverage


class HouseBlend(Beverage.Beverage):
    """HouseBlend"""

    def __init__(self):
        self._description = 'House Blend (1.5$)'
        self._cost = 1.5
