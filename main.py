import requests as rq
from twilio.rest import Client
import os

Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("WEATHER_API_KEY")
account_sid = "AC77812d86d34bccafde0f51f523235923"
auth_token = os.environ.get("AUTH_TOKEN")
parameters = {
    'lat':-18.030,
    'lon':-41.119,
    "units":"metric",
    "cnt":4,
    "appid":api_key,
}

response = rq.get(Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="There will be rain in the next 12 Hours",
        from_="+16014363633",
        to="+5553981613401",
    )
print(message.status)