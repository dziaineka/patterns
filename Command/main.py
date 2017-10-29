import asyncio
import remoteControl
import remoteLoader


controller = remoteControl.RemoteControl()
remoteLoader.setup_controller(controller)

my_event_loop = asyncio.get_event_loop()

try:
    tasks = [
                # controller.on_button_pushed(0),
                # controller.on_button_pushed(1),
                controller.on_button_pushed(2),

                # controller.off_button_pushed(0),
                # controller.off_button_pushed(1),
                controller.off_button_pushed(2),
            ]

    my_event_loop.run_until_complete(asyncio.wait(tasks))
finally:
    my_event_loop.close()


