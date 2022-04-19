from datetime import datetime
from utils.consts import DATETIME_FORMAT
from utils.helpers import convert_wind_speed, temp_from_kelvin_to_celcius


class WeatherObject():
    def __init__(self, weather):
        datetime_obj = datetime.utcfromtimestamp(weather['dt'])
        self.time = datetime_obj.strftime(DATETIME_FORMAT)
        self.day = datetime_obj.strftime("%d")
        self.hour = datetime_obj.strftime("%H:%M")
        self.main_weather = weather['weather'][0]['main']
        self.weather_description = weather['weather'][0]['description']
        self.clouds = weather['clouds']
        self.temp = temp_from_kelvin_to_celcius(weather['temp'])
        self.feels_like = temp_from_kelvin_to_celcius(weather['feels_like'])
        self.pressure = weather['pressure']
        self.humidity = weather['humidity']
        self.wind_speed = weather['wind_speed']
        self.wind_speed_converted = convert_wind_speed(self.wind_speed)
