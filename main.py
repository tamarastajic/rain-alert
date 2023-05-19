from twilio.rest import Client
import requests

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Open Weather API ~~~~~~~~~~~~~~~~~~~~~~~~~
OW_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
# Input your own data!
api_key = YOUR OPEN WEATHER API KEY

weather_parameters = {
    "lat": YOUR LAT,
    "lon": YOUR LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OW_Endpoint, params=weather_parameters)
response.raise_for_status()

weather = response.json()

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Twilio API ~~~~~~~~~~~~~~~~~~~~~~~~~
# Input your own data!
account_sid = YOUR TWILIO SID
auth_token = YOUR TWILIO AUTH TOKEN
from_number = SENDER NUMBER
to_number = RECIPIENT NUMBER

# Will it Rain?
will_rain = False

for i in range(0, 12):
    weather_id = weather["hourly"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
        break

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Sending an SMS ~~~~~~~~~~~~~~~~~~~~~~~~~
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It will rain so bring an umbrella! ☔",
            from_= from_number,
            to= to_number
                )
    print(message.status)
