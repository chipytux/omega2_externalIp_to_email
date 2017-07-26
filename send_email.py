#!/usr/bin/python

import smtplib
import subprocess
import urllib2
from email.mime.text import MIMEText



smtp_address="YOUR SMTP LOGIN"
sender="YOUR SMTP LOGIN "
receiver="YOUR EMAIL DESTINATION"
password="YOURU SMTP PASSWORD"

uptime =  subprocess.check_output('uptime')
ip_ext = urllib2.urlopen("http://ifconfig.me/ip").read()
print ip_ext
#ip_ext =  subprocess.check_output(['curl','ifconfig.me'])

msg = MIMEText(uptime+ip_ext)
msg ["Subject"] = "Onion Report"
server = smtplib.SMTP(smtp_address)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,msg.as_string())
server.quit()
