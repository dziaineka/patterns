import Observer


class WeatherForecast(Observer.Observer):
    """forecast for tomorrow"""

    def __init__(self):
        super(WeatherForecast, self).__init__()
        self.temperatures = []
        self.humidities = []
        self.pressures = []

    def show_forecast(self):
        print()
        print('Forecast for tommorow:')
        print('temp: {}'.format(self.temperature))
        print('humidity: {}'.format(self.humidity))
        print('pressure: {}'.format(self.pressure))
        print()

    def get_average(self, parameters):
        items_count = 0
        items_sum = 0

        for param in parameters:
            items_count += 1
            items_sum += param

        return items_sum / items_count

    def collect_data(self, temperature, humidity, pressure):
        self.temperatures.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)

        if len(self.temperatures) == 10:
            self.temperature = self.get_average(self.temperatures)
            self.humidity = self.get_average(self.humidities)
            self.pressure = self.get_average(self.pressures)

            self.temperatures.clear()
            self.humidities.clear()
            self.pressures.clear()

            return True
        else:
            return False

    def update(self, temperature, humidity, pressure):
        if self.collect_data(temperature, humidity, pressure):
            self.show_forecast()
