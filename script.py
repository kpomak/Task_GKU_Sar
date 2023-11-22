import asyncio

from app.core import WeatherForecast


async def parse():
    parser = WeatherForecast()
    await parser.get_weather()
    parser.save_weather_data()


if __name__ == "__main__":
    asyncio.run(parse())
