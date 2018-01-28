import email
import smtplib
from urllib2 import urlopen
from datetime import date
import os.path

SMTPServer = ""  # Enter the smtp server
SMTPPort = 000  # Enter smtp server port number
myEmail = ""  # Email you wish to be sender
targetEmail= ""  # Email that is the target
my_ip = urlopen('http://ip.42.pl/raw').read()  # Retrieves external IP, you can change source

# Creates email object
msg = email.message_from_string("IP adress for " + str(date.today()) + " is: " + my_ip)
msg['From'] = "From"
msg['To'] = "To"
msg['Subject'] = "IP Address"

server = smtplib.SMTP(SMTPServer, SMTPPort)
server.ehlo()  # Hostname to send for this command defaults to the fully qualified domain name of the local host.
server.starttls()  # Puts connection to SMTP server in TLS mode
server.ehlo()
server.login(myEmail, "Enter email pass")  # TODO Create safer way for this information to be input

server.sendmail(myEmail, [targetEmail], msg.as_string())
server.quit()

# Creates a txt log file for local storage
# Recommend directing file to a cloud location or run script from cloud
if os.path.exists("log.txt"):
    logFile = open("log.txt", "a")
    logFile.write("\n[" + str(date.today()) + "] " + my_ip)
    logFile.close()
else:
    logFile = open("log.txt", "w")
    logFile.write("\n[" + str(date.today()) + "] " + my_ip)
    logFile.close()