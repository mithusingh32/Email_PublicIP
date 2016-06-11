import email
import smtplib
from urllib2 import urlopen
import time
from datetime import date

my_ip = urlopen('http://ip.42.pl/raw').read()


msg = email.message_from_string("IP adress for "+ str(date.today()) + " is: "+ my_ip)
msg['From'] = "From"
msg['To'] = "To"
msg['Subject'] = "IP Address"

server = smtplib.SMTP("smtp.live.com",587)
server.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
server.starttls() #Puts connection to SMTP server in TLS mode
server.ehlo()
server.login('email address', 'password')

server.sendmail("your email address again", ["Who you're sending to"], msg.as_string())

server.quit()