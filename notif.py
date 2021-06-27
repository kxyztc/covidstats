import pip
pip install requests
pip install plyer
import ctypes
import datetime
import time
import requests
from plyrs import notification
# matches = sports.get_sport(sports.SOCCER)
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/canada")
except:
    ctypes.windll.user32.MessageBoxW(0, "Please try again", "Error!", 1)

if (covidData !=None):
    data = covidData.json()['Success']
    while(True):
        notification.notify(
            title = "COVID19 Stats in {}".format(datetime.date.today()),
            message = "Total Cases: {totalcases}\nToday Cases: {todaycases}\n Today Deaths: {todaydeaths}".format(
                totalcases = data['cases'],
                todaycases = data["todaycases"],
                todaydeaths = data ["todaydeaths"]),

            app_icon = "Paomedia-Small-N-Flat-Bell.ico",
            timeout = 50
        )
        time.sleep(60*60*4)
