from Commands import command


class RemoteControl:
    def __init__(self):
        no_command = command.Command()
        self.on_commands = [no_command, no_command, no_command]
        self.off_commands = [no_command, no_command, no_command]

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    async def on_button_pushed(self, slot):
        await self.on_commands[slot].execute()

    async def off_button_pushed(self, slot):
        await self.off_commands[slot].execute()



