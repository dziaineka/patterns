class DoorLock:
    """door lock managing (lock/unlock)"""

    def __init__(self):
        self.__locked = 0
        self.__unlocked = 1
        self.state = self.__unlocked

    def lock(self):
        self.state = self.__locked
        print('Door is locked now.')

    def unlock(self):
        self.state = self.__unlocked
        print('Door is unlocked now.')
