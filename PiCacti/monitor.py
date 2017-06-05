from time import sleep

import schedule

from PiCacti.weatherChecker import WeatherChecker

wc = WeatherChecker()
history = []  # Temperature history
can_go_outside = False
MAX_RAIN = 10  # Millimeters
MIN_TEMP = 50  # degrees Fahrenheit


def check():
    global history, can_go_outside
    if len(history) > 31:  # more than a months history
        history = history[-31:]  # reduce to the last month

    if wc.is_too_cold(MIN_TEMP):
        history.append(False)
        can_go_outside = False
    else:
        if wc.get_todays_rain() > MAX_RAIN:  # more than 10 mm : probably too rainy
            history.append(False)
            can_go_outside = False
        else:
            history.append(True)
            can_go_outside = True

    if len(history) < 7:
        # short history
        temp_past_week = history
    else:
        # get last weeks worth
        temp_past_week = history[-7:]

    if all(temp_past_week):
        # if the last week has been nice, do nothing
        pass
    elif any(temp_past_week) and can_go_outside:
        # weather has been changing, but today is acceptable
        # TODO - send email
        pass
    else:
        # weather is too cold and has been too cold
        pass

schedule.every().day.at("5:00").do(check)

while True:
    schedule.run_pending()
    sleep(1)  # wait
