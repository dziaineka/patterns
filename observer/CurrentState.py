import Observer


class CurrentState(Observer.Observer):
    """shows current weather params"""

    def update(self, temperature, humidity, pressure):
        def show_current_weather():
            print()
            print('Current weather')
            print('temp: {}'.format(temperature))
            print('humidity: {}'.format(humidity))
            print('pressure: {}'.format(pressure))
            print()

        show_current_weather()
