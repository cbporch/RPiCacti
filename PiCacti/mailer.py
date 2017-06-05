import smtplib
import json

from email.mime.text import MIMEText


class Mailer:
    def __init__(self):
        # read parameters from JSON file
        with open('secrets.json', 'r') as fp:
            secrets_json = json.load(fp)
        self.SENDER = secrets_json["sender-email"]

    def send_mail(self):
        pass
