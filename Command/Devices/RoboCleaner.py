import asyncio


class RoboCleaner:
    """RoboCleaner"""

    def __init__(self):
        self.__off = 0
        self.__working = 1
        self.__idle = 2
        self.state = self.__off

    def switch_off(self):
        self.state = self.__off
        print('Robo is switched off now.')

    def switch_on(self):
        self.state = self.__idle
        print('Robo is switched on now.')

    async def clean(self):
        if self.state == self.__working:
            print('Robo is working now.')
        else:
            self.state = self.__working
            print('Robo is starting work.')
            await asyncio.sleep(10)
            print('Robo is ending work.')
            self.state = self.__idle
