from Commands import command


class RoboCleanCommand(command.Command):
    def __init__(self, robo):
        self.robo = robo

    async def execute(self):
        self.robo.switch_on()
        await self.robo.clean()


class RoboSwitchOffCommand(command.Command):
    def __init__(self, robo):
        self.robo = robo

    async def execute(self):
        await self.robo.switch_off()
