import pandas as pd
import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
# df = pd.read_csv("weather_data.csv")

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()

# data = response.json()

# lat = data["iss_position"]["latitude"]
# long = data["iss_position"]["longitude"]

# position = (lat, long)
# print(position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
time_now = datetime.now()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)
print(time_now.hour)