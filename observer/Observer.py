class Observer:
    """basic class for observers"""

    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def update(self, temperature, humidity, pressure):
        print('Hello from base class')

