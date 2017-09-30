import random
import time


class WeatherData:
    """returns random temperature"""

    @staticmethod
    def get_temperature():
        return random.randint(-30, 40)

    @staticmethod
    def get_humidity():
        return random.randint(0, 100)

    @staticmethod
    def get_pressure():
        return random.randint(700, 800)

    def measurements_changed(self):
        print('temperature: {} humidity: {} pressure: {}'.format(
            self.get_temperature(),
            self.get_humidity(),
            self.get_pressure())
        )

    def start_work(self):
        while True:
            time.sleep(random.randint(0, 10))
            self.measurements_changed()
