from Devices import *
from Commands import *


def setup_controller(remote_control):
    door = doorLock.DoorLock()
    tmp_light = light.Light()
    robo = roboCleaner.RoboCleaner()

    door_lock_command = doorCommands.DoorLockCommand(door)
    door_unlock_command = doorCommands.DoorUnlockCommand(door)

    light_on_command = lightCommands.LightOnCommand(tmp_light)
    light_off_command = lightCommands.LightOffCommand(tmp_light)

    robo_clean_command = roboCleanerCommands.RoboCleanCommand(robo)
    robo_off_command = roboCleanerCommands.RoboSwitchOffCommand(robo)

    remote_control.set_command(0, door_lock_command, door_unlock_command)
    remote_control.set_command(1, light_on_command, light_off_command)
    remote_control.set_command(2, robo_clean_command, robo_off_command)
