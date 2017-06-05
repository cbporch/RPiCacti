import smtplib
import json

from email.mime.text import MIMEText


class Mailer:
    def __init__(self):
        # read parameters from JSON file
        with open('/RPiCacti/RPiCacti/PiCacti/secrets.json', 'r') as fp:
            secrets_json = json.load(fp)
        self.SENDER = secrets_json["sender-email"]
        self.SENDERPASS = secrets_json["sender-pass"]
        self.RECEIVER = secrets_json["rec-email"]


    def send_mail(self, inside=True):
        if inside:
            # bring inside message
            with open("messages/inside.txt") as file:
                msg = file.read()
        else:
            # send outside
            with open("messages/outside.txt") as file:
                msg = file.read()

        msg = MIMEText("""{2}""".format(self.SENDER, self.RECEIVER, msg))

        msg['Subject'] = 'PiCacti'
        msg['From'] = self.SENDER
        msg['To'] = self.RECEIVER

        try:
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login(self.SENDER, self.SENDERPASS)
            s.sendmail(self.SENDER, self.RECEIVER, msg.as_string())
        except smtplib.SMTPException:
            # something broke
            print("unable to send mail")

    def mail_test(self):
        msg = MIMEText("""Test""".format(self.SENDER, self.RECEIVER))

        msg['Subject'] = 'PiCacti'
        msg['From'] = self.SENDER
        msg['To'] = self.RECEIVER

        try:
            print(self.SENDER)
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login(self.SENDER, self.SENDERPASS)
            s.sendmail(self.SENDER, self.RECEIVER, msg.as_string())
            print("message sent!")
        except smtplib.SMTPException:
            # something broke
            print("unable to send mail")
            raise

m = Mailer()
m.mail_test()
