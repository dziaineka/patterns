import random
import asyncio
import Subject


class WeatherData(Subject.Subject):
    """returns random temperature"""

    def __init__(self):
        super(WeatherData, self).__init__()
        self.get_params()

    @staticmethod
    def get_temperature():
        return random.randint(-30, 40)

    @staticmethod
    def get_humidity():
        return random.randint(0, 100)

    @staticmethod
    def get_pressure():
        return random.randint(700, 800)

    def get_params(self):
        self.temperature = WeatherData.get_temperature()
        self.humidity = WeatherData.get_humidity()
        self.pressure = WeatherData.get_pressure()

    def measurements_changed(self):
        self.notify_observers()

    async def start_work(self):
        while True:
            await asyncio.sleep(random.randint(0, 10))
            self.get_params()
            self.measurements_changed()
