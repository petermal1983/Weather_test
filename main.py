import requests
import json
from datetime import datetime

longitude = 60.60570250000001
latitude = 56.83892609999999

pressure_arr = []

temperature_diff = []

days = []

API_KEY = "4093ec862453addcda158d1e9f728d49"

api_response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon="
    f"{longitude}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric&lang=ru").text
json_response = json.loads(api_response)

for i in range(4):
    pressure_arr.append(json_response["daily"][i]["pressure"])

pressure_arr.append(json_response["current"]["pressure"])

for i in range(5):
    temperature_diff.append(json_response["daily"][i]["temp"]["day"] - json_response["daily"][i]["temp"]["night"])

for i in range(5):
    days.append(json_response["daily"][i]["dt"])

timestamp = days[temperature_diff.index(min(temperature_diff))]

our_date = datetime.utcfromtimestamp(timestamp).strftime('%Y/%m/%d')

print("Максимальное прогнозируемое давление за пять дней, включая текущий:", max(pressure_arr) * 0.750063755419211,
      "мм.рт.ст."
      '\n'"День с минимальной разницей между ночной и дневной температурой согласно прогнозу:", min(temperature_diff),
      "град. Цельсия - ",
      our_date)
