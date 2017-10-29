import asyncio


class DoorLock:
    """door lock managing (lock/unlock)"""

    def __init__(self):
        self.__locked = 0
        self.__unlocked = 1
        self.state = self.__unlocked

    async def lock(self):
        await asyncio.sleep(2)
        self.state = self.__locked
        print('Door is locked now.')

    async def unlock(self):
        await asyncio.sleep(2)
        self.state = self.__unlocked
        print('Door is unlocked now.')
