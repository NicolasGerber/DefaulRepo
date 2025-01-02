import requests as rq
from datetime import datetime
import smtplib

my_email = "pythongerber@gmail.com"
password="rsev zovr jhww otlm"

MY_LAT =-31.758625
MY_LNG =-52.305597

response = rq.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data_iss = response.json()

iss_latitude = float(data_iss["iss_position"]["latitude"])
iss_longitude = float(data_iss["iss_position"]["longitude"])


parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

var = rq.get("https://api.sunrise-sunset.org/json", params=parameters)
var.raise_for_status()
data = var.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time = int(time_now.timestamp())

if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_latitude <= MY_LNG + 5 :
    if sunset > time:
         with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=my_email,password=password)
             connection.sendmail(from_addr=my_email,
                                 to_addrs=my_email,
                                 msg="Subject:LOOK UP\n\nLook up at the sky the ISS is passing by NOW")
