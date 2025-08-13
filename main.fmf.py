import requests
import pandas as pd
from datetime import datetime

API_KEY = "tvoj_api_kljuc"  # pridobi ga iz OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def fetch_weather(city, units="metric"):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    records = []
    for entry in data["list"]:
        records.append({
            "city": city,
            "datetime": datetime.fromtimestamp(entry["dt"]),
            "temperature": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "weather": entry["weather"][0]["main"]
        })
    
    return pd.DataFrame(records)

fetch_weather("Ljubljana")
