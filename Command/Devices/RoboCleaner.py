import asyncio


class RoboCleaner:
    """RoboCleaner"""

    def __init__(self):
        self.__off = 0
        self.__working = 1
        self.__idle = 2
        self.state = self.__off

    async def switch_off(self):
        await asyncio.sleep(3)
        self.state = self.__off
        print('Robo is switched off now.')

    def switch_on(self):
        self.state = self.__idle
        print('Robo is switched on now.')

    async def completed(self):
        rooms = 11
        timer = rooms - 1
        while self.state != self.__off and timer != 0:
            await asyncio.sleep(1)

            print('{} room has been cleaned.'.format(rooms - timer))

            timer -= 1
            if timer == 0:
                return True

        return False

    async def clean(self):
        if self.state == self.__working:
            print('Robo is working now.')
        else:
            self.state = self.__working
            print('Robo is starting work.')
            if await self.completed():
                print('Robo is ending work.')
                self.state = self.__idle
            else:
                print('Robo has been switched off.')
