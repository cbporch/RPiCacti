import smtplib
import json

from email.mime.text import MIMEText


class Mailer:
    def __init__(self):
        # read parameters from JSON file
        with open('secrets.json', 'r') as fp:
            secrets_json = json.load(fp)
        self.SENDER = secrets_json["sender-email"]
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

        msg = MIMEText("""From: Raspberry Pi <{0}>
        To: Your Name <{1}>
        Subject: PiCacti
        
        {2}
        """.format(self.SENDER, self.RECEIVER, msg))

        try:
            s = smtplib.SMTP('localhost')
            s.sendmail(self.SENDER, self.RECEIVER, msg)
        except smtplib.SMTPException:
            # something broke
            print("unable to send mail")

    def mail_test(self):
        msg = MIMEText("""From: Raspberry Pi <{0}>
                To: Your Name <{1}>
                Subject: PiCacti

                Test
                """.format(self.SENDER, self.RECEIVER))

        try:
            s = smtplib.SMTP('localhost')
            s.sendmail(self.SENDER, self.RECEIVER, msg)
            print("message sent!")
        except smtplib.SMTPException:
            # something broke
            print("unable to send mail")

m = Mailer
m.mail_test()