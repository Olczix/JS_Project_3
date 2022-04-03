from PyQt5.QtWidgets import *
from api.weather import *
from utils.helpers import *
from api.weather import *


def about_creator() -> None:
    mbox = QMessageBox()
    mbox.setText("Wykonawca: Aleksandra Barska\nWersja: 1.0")
    mbox.setStandardButtons(QMessageBox.Ok)
    mbox.exec_()

def about_used_api() -> None:
    mbox = QMessageBox()
    mbox.setText("Aplikacja pogodowa korzystająca z API OpenWeatherMap")
    mbox.setStandardButtons(QMessageBox.Ok)
    mbox.exec_()

def about_app_trigger(q) -> None:
    if q.text() == "O twórcy":
        about_creator()
    elif q.text() == "Więcej o OpenWeatherMap":
        about_used_api()

def get_current_weather():
    city = get_city_from_file()
    if city != "":
        weather = get_weather_by_city_name(city)
        main_weather = weather['weather'][0]['main']
        weather_description = weather['weather'][0]['description']
        clouds = weather['clouds']['all']
        temp = temp_from_kelvin_to_celcius(weather['main']['temp'])
        feels_like = temp_from_kelvin_to_celcius(weather['main']['feels_like'])
        min_temp = temp_from_kelvin_to_celcius(weather['main']['temp_min'])
        max_temp = temp_from_kelvin_to_celcius(weather['main']['temp_max'])
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        return temp, min_temp, max_temp, feels_like, main_weather, weather_description, \
            clouds, wind_speed, pressure, humidity
    else:
        # TODO: handle no city in file 
        print("NO CITY SPECIFIED!")


def get_weather_trigger(q) -> None:
    if q.text() == "Aktualna pogoda":
        return get_current_weather()
    elif q.text() == "Pogoda na 3 dni":
        about_used_api()
