import Beverage


class DarkRoast(Beverage.Beverage):
    """DarkRoast"""

    def __init__(self):
        self._description = 'Dark Roast (2$)'
        self._cost = 2
