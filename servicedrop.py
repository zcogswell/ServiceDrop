#/usr/bin/python3

from os import system
from sys import argv
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import *

from datetime import datetime as dt


ROUTER = '192.168.1.1'              # router IP for LAN checking
SENDER = 'example1@gmail.com'       # sending email address
PASSWORD = argv[1]                  # sending email password
RECEIVER = 'example2@gmail.com'     # receiving email address
SMTP_ADDR = 'smtp.gmail.com'        # email server
SMTP_PORT = 465                     # email server port number
WAIT = 60                           # number of seconds between consecutive requests

# information in the email, string formatting will place beginning and end time of outage
SUBJECT = 'Internet is down.'
BODY = """The internet connectivity at my house was currently down at %s until %s."""

while True:
    # check internet connection
    response = system('ping -c4 %s > /dev/null' % SMTP_ADDR)
    if response != 0:
        # check LAN connection
        response = system('ping -c4 %s > /dev/null' % ROUTER)
        if response == 0:
            print('No internet connectivity. Emailing ISP.')
            time1 = dt.now()
            # wait until connection is regained to send mail
            while system('ping -c4 %s > /dev/null' % SMTP_ADDR) != 0:
                print('Still down')
                sleep(WAIT)
            time2 = dt.now()

            try:
                server = SMTP_SSL(host=SMTP_ADDR, port=SMTP_PORT)
                server.login(SENDER, PASSWORD)
                msg = MIMEMultipart()
                msg['From'] = SENDER
                msg['To'] = RECEIVER
                msg['Subject'] = SUBJECT
                msg.attach(MIMEText(BODY % (time1, time2), 'plain'))
                server.send_message(msg)
                del msg
                server.quit()
            except SMTPHeloError as e:
                print('Email server failure: %s' % e)
        else:
            print('No LAN connectivity.')
    sleep(WAIT)
    