from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
WEATHER_API_URL = os.getenv("WEATHER_API_URL")  

def get_weather(city="London"):
    url = f"{WEATHER_API_URL}?appid={API_KEY}&q={city}&units=metric"
    weather_data = requests.get(url).json()
    return weather_data



if __name__ == "__main__":
    print("***Get Current Weather Data***")
    city = input("Please, enter a city name: ").strip()
    if not bool(city.strip()) or not city or city == "":
        city = "London"

    weather_data = get_weather(city)
    pprint(weather_data)