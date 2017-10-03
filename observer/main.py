import WeatherData
import CurrentState
import WeatherForecast
import asyncio


async def timer():
    second = 1

    while True:
        await asyncio.sleep(1)
        print('{} sec'.format(second))
        second = second + 1


weather_station = WeatherData.WeatherData()
current_state = CurrentState.CurrentState()
weather_forecast = WeatherForecast.WeatherForecast()
my_event_loop = asyncio.get_event_loop()

weather_station.register_observer(current_state, weather_forecast)

try:
    tasks = [timer(), weather_station.start_work()]
    my_event_loop.run_until_complete(asyncio.wait(tasks))
finally:
    my_event_loop.close()
