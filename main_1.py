import requests
from datetime import datetime
import smtplib


my_email = "agataaduckiewicz@gmail.com" # this is a test email
password = "please use your email and password"

MY_LAT = "please use your latitude for location"
MY_LONG = "please use your longitude for location"



def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    print(iss_latitude)
    iss_longitude = float(data["iss_position"]["longitude"])

    # (for testing purpose you can use iss location as your location)
    # iss_latitude = MY_LAT
    # iss_longitude = MY_LONG


    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted":0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    # for testing purpose you can use your sunset time as time now
    # time_now = 18

    if time_now >= sunset or time_now <= sunrise:
        return True
# while True:
#     time.sleep(60)
if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr="agataaduckiewicz@gmail.com",to_addrs="agataaduckiewicz@gmail.com", msg="Subject:Look UP\n\n The ISS is above you in the sky"
                        )










