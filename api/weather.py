from utils.consts import WEATHER_API_URL, API_KEY
import requests
from typing import Dict, Any
from api.geo import get_city_geo_location


def get_weather_by_city_name(name: str) -> Dict[str, Any]:
    lat, lon = get_city_geo_location(name)
    url = f"{WEATHER_API_URL}lat={lat}&lon={lon}&appid={API_KEY}"
    return requests.get(url).json()
