from Commands import command


class DoorLockCommand(command.Command):
    def __init__(self, door_lock):
        self.door_lock = door_lock

    async def execute(self):
        await self.door_lock.lock()


class DoorUnlockCommand(command.Command):
    def __init__(self, door_lock):
        self.door_lock = door_lock

    async def execute(self):
        await self.door_lock.unlock()
