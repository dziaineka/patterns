class Light:
    """switch the light on/off"""

    def __init__(self):
        self.__off = 0
        self.__on = 1
        self.state = self.__off

    def switch_off(self):
        self.state = self.__off
        print('Light is switched off now.')

    def switch_on(self):
        self.state = self.__on
        print('Light is switched on now.')
