import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):

    api_key = os.getenv("WEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    # Check if API returned valid weather data
    if "weather" not in data:
        return "Weather data not available"

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    return f"{round(temp)}°C, {weather}"