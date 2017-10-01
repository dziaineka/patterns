import WeatherData
import asyncio


async def timer():
    second = 1

    while True:
        await asyncio.sleep(1)
        print('{} sec'.format(second))
        second = second + 1


weather_station = WeatherData.WeatherData()
my_event_loop = asyncio.get_event_loop()

try:
    tasks = [timer(), weather_station.start_work()]
    my_event_loop.run_until_complete(asyncio.wait(tasks))
finally:
    my_event_loop.close()

