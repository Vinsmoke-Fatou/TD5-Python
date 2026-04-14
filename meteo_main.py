import requests

API_KEY = "d568c02d9d90723ccc92c73dbb88328e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
VILLE = "Dakar"

params = {
    "q": VILLE,
    "appid": API_KEY,
    "units": "metric",
    "lang": "fr"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidite = data["main"]["humidity"]
    print(f"Météo à {VILLE}:")
    print(f"  -- Température : {temperature}°C")
    print(f"  -- Description : {description}")
    print(f"  -- Humidité    : {humidite}%")
else:
    print(f"Erreur : {response.status_code}")
    print(response.text)