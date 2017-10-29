from Commands import command


class LightOnCommand(command.Command):
    def __init__(self, light):
        self.light = light

    async def execute(self):
        await self.light.switch_on()


class LightOffCommand(command.Command):
    def __init__(self, light):
        self.light = light

    async def execute(self):
        await self.light.switch_off()
