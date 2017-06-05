# PiCacti

**Current Status:**  Nonfunctional _- 6/5/17_

A simple program that checks the weather and sends an email to you if the temperature will be 
below a certain threshold. Designed for use on a web-connected Raspberry Pi.

To setup PiCacti, modify the file called `NEWsecrets.json` in the PiCacti directory, with the following changes:

    {
      "sender-email": "SENDER-EMAIL",
      "rec-email": "EMAIL",
      "API-key": "KEY",
      "zipcode": "ZIP",
      "country": "COUNTRY",
      "city-id": "CITY-ID"
    }

- Replace `SENDER-EMAIL` with an email account to do the sending.
- Replace `PASSWORD` with the password for that account
- Replace `EMAIL` with the account to be notified
- Replace `KEY` with a valid [OpenWeatherMap](https://www.openweathermap.org/) API key
- Replace `CITY-ID` with a City ID code for a city close to you: [check here](http://openweathermap.org/help/city_list.txt)
- Finally, rename the file to `secrets.json`