from PyQt5.QtWidgets import *
from api.weather import *
from utils.helpers import *
from api.weather import *
from py_gtk_app.app import start_gtk_app
from utils.weather_object import WeatherObject


def info_box(msg: str) -> None:
    mbox = QMessageBox()
    mbox.setText(msg)
    mbox.setStandardButtons(QMessageBox.Ok)
    mbox.exec_()


def error_box(msg: str) -> None:
    mbox = QMessageBox()
    mbox.setText(msg)
    mbox.setStandardButtons(QMessageBox.Ok)
    mbox.exec_()


def about_app_trigger(q) -> None:
    if q.text() == "O twórcy":
        info_box("Wykonawca: Aleksandra Barska\nWersja: 1.0")
    elif q.text() == "Więcej o OpenWeatherMap":
        info_box("Aplikacja pogodowa korzystająca z API OpenWeatherMap")


def get_current_weather_obj():
    city = get_city_from_file()
    if city != "":
        weather = get_weather_by_city_name(city)
        return WeatherObject(weather["current"])
    else:
        error_box("Brak zdefiniowanego miasta.\nMusisz je wybrać, aby korzystać z prognozy pogody.")


def get_hourly_weather_list():
    city = get_city_from_file()
    if city != "":
        weather = get_hourly_weather_by_city_name(city)
        weather_hourly_list = weather["hourly"]
        weather_list = []
        for weather_hourly in weather_hourly_list:
            weather_list.append(WeatherObject(weather_hourly))
        return weather_list
    else:
        error_box("Brak zdefiniowanego miasta.\nMusisz je wybrać, aby korzystać z prognozy pogody.")
