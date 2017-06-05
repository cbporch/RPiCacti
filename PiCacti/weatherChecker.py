from datetime import datetime, timedelta, time

import pyowm
import json


class WeatherChecker:

    def __init__(self):
        # read parameters from JSON file
        with open('secrets.json', 'r') as fp:
            secrets_json = json.load(fp)
        self.API_KEY = secrets_json["API-key"]
        # self.ZIPCODE = secrets_json["zipcode"]
        # self.COUNTRY = secrets_json["country"]
        self.CITY_ID = secrets_json["city-id"]
        # open connection to OpenWeatherMap
        self.owm = pyowm.OWM(self.API_KEY)

    def is_too_cold(self, mintemp=50):
        observation = self.owm.weather_at_id(int(self.CITY_ID))
        temps = observation.get_weather().get_temperature('fahrenheit')
        low = temps['temp_min']
        if low < mintemp:
            # too cold for cacti
            return True
        return False

    def get_todays_rain(self):
        # TODO - check for rain
        forecast = self.owm.three_hours_forecast_at_id(int(self.CITY_ID))
        today = datetime.today()
        eight = time(8, 0, 0, tzinfo=today.tzinfo)
        tomorrow = datetime.combine((today + timedelta(days=1)).date(), time=eight)
        today_and_overnight_rain = 0
        tom_rain = 0

        for f in forecast.get_forecast():
            fcst_t = f.get_reference_time(timeformat='date')
            fcst_time = time(today.time().hour, tzinfo=today.tzinfo)
            fcst_t = datetime.combine(fcst_t.date(), fcst_time)
            if fcst_t.date() == today.date() \
                    or today < fcst_t < tomorrow:
                today_and_overnight_rain += f.get_rain().get('3h', 0)
            elif fcst_t.date() == tomorrow.date():
                tom_rain += f.get_rain().get('3h', 0)
            # print(str(f.get_reference_time(timeformat='date')) + " " + str(f.get_rain().get('3h', 0)))
        # print("Today's rain: {0} mm".format(today_and_overnight_rain))
        # print("Tomorrow's rain: {0} mm".format(tom_rain))
        return today_and_overnight_rain
