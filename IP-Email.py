#IP-Email.py (v3.5)
#Get at https://github.com/Protocol73/Email-IP
#For use w/ Python  v2.7 & v3.7, Eip-Settings.cfg & address.cfg

import os
import sys

print("Getting Ready")

def cls(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
cls() 

import time #Used for time.sleep
import smtplib #For conecting to smtp Server

try: #for py v2 vs v3 input
    input = raw_input
except NameError:
    pass

#for using cfg files
try:
    import ConfigParser# Python 2
except ImportError:
    from configparser import ConfigParser
    import configparser as ConfigParser
try: #for Python smtp usage
    from email.MIMEText import MIMEText
    from email.MIMEMultipart import MIMEMultipart
except ImportError:
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

from email import encoders
from datetime import datetime #for timestamps

#import Settings from Eip-Settings.cfg
cfg_settings = ConfigParser.RawConfigParser()
configFilePath = r'Eip-Settings.cfg'
cfg_settings.read(configFilePath)

subject = cfg_settings.get('Settings', 'subject')
Prompt1 = cfg_settings.get('Settings', 'Prompt1')
Prompt2 = cfg_settings.get('Settings', 'Prompt2')
var1text = cfg_settings.get('Settings', 'var1text')
var2text = cfg_settings.get('Settings', 'var2text')
beforeIPText = cfg_settings.get('Settings', 'beforeIPText')
afterIPText = cfg_settings.get('Settings', 'afterIPText')
fromaddr = cfg_settings.get('Settings', 'fromaddr')
password = cfg_settings.get('Settings', 'password')

#define the main checks

def CheckInput(): #To Help w/ Mistyped IP's
    if IP == IP2:
        return True
    else:
        return False
        CheckInput = False
    pass
cls()

def Validate_IP(s): #checks for valid looking IP address.
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

IP = input(Prompt1) #First Prompt
IP2 = input(Prompt2)#Check Prompt

#Imput Checks Logic

if CheckInput() == True:
    pass
else:
    print("Error: Those IP's Don't Match.")
    time.sleep(2)

if Validate_IP(IP) == True:
    time.sleep(1.5)
else:
    print("Error:" + IP + " did NOT appear to be a valid IP address.")
    time.sleep(2) 

if CheckInput() & Validate_IP(IP) == True:
    cls()
    print ("Accepted IP: " + IP)
else: # Ask to Restart if there was errors in the input
    print("Restart?")
    restart = input("y/n:")
    if restart in ['y' or 'yes']:
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif restart in ['n' or 'no']:
        print("Goodbye")
        time.sleep(1)
        sys.exit()
    else:
        print("Invalid Input,Quiting")
        time.sleep(1)
        sys.exit()

#checks done so..
#Get the last input fom the user 

var1 = input(var1text)
var2 = input(var2text) 

#import address.cfg
cfg_addr = ConfigParser.RawConfigParser()
configFilePath = r'address.cfg'
cfg_addr.read(configFilePath)
#Get Email Ready
to = cfg_addr.get('address', 'to')
cc = to = cfg_addr.get('address', 'cc')
rcpt = cc.split(",") + [to]
msg = MIMEMultipart()
msg['subject'] = subject
msg['cc'] = cc
msg['to'] = to

#Tack it all together & format it.
body1 = (beforeIPText + " " + IP + " " + afterIPText + "\r\n \r\n" + var1text + var1 + "\r\n" + var2text + var2 + "\r\n")

msg.attach(MIMEText(body1, 'plain'))

#Connect & login to email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print("Logging In..")
server.login(fromaddr, password)
text = msg.as_string()
print("Sending Email...")
server.sendmail(fromaddr,rcpt,text)
server.quit()
#Email Done

# Log Notice
naive_dt = datetime.now() #set datetime to local timezone
print ("Logging to file at: ")
print(datetime.now().strftime("%a, %d %B %Y %I:%M"))
time.sleep(1)

# Storage & info for Log File
newline = ["\n"]  #for formating
text_install = ["Installed & Emailed out:"]
text_ip = [IP]
endtxt = [" ----- Device Divider ----- "]
# file name & how to open it,will be created on first successful run
LogFileName = "Install Log.txt" #Change File Name to Whatever you  want.
fh = open(LogFileName, "a")
# End Data Storage

# log data to file
fh.writelines(newline)
fh.writelines(newline)
fh.writelines(datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
fh.writelines(newline)
fh.writelines(newline)
fh.writelines(text_install)
fh.writelines(newline)
fh.writelines(text_ip)
fh.writelines(newline)
fh.writelines(endtxt)
fh.close
print ("Device: " + IP + " Added to log & emailed" )
print ('Done')
time.sleep(5)
sys.exit(0)