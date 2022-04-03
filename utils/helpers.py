from utils.consts import CITY_FILE_PATH
import os


def get_city_from_file() -> str:
    path = os.path.join(os.getcwd(), CITY_FILE_PATH)
    with open(path, 'r') as city_file:
        city_name = city_file.read()
    return city_name

def temp_from_kelvin_to_celcius(temp: str) -> str:
    temp_k = float(temp)
    temp_c = round(temp_k - 273.15, 2)
    return str(temp_c)

def convert_wind_speed(wind_speed: float) -> float:
    return round(wind_speed/1000*3600, 2)
