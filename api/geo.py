from utils.consts import GEO_API_URL, API_KEY
import requests


def get_city_geo_location(name: str = "", state_code: str = "",
    country_code: str = ""):
    url = f"{GEO_API_URL}q={name},{state_code},{country_code}&limit=5&appid={API_KEY}"
    response = requests.get(url).json()[0]
    return response['lat'], response['lon']
