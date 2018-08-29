#IP-Email.py
#Get at https://github.com/Protocol73/Email-IP
#For use w/ Python 3.7 , StoredData.py & address.py 

import os
import sys

print("Getting Ready")

def cls(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
cls() 

import time
import smtplib
import address as email
import StoredData as SD
from email import encoders
from datetime import datetime
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart

def CheckInput(): #To Help w/ Mistyped IP's
    if IP == IP2:
        return True
    else:
        return False
        CheckInput = False
    pass
cls()

#This Block checks for valid looking IP address.
def Validate_IP(s): 
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

IP = raw_input(SD.Prompt1) #First Prompt
IP2 = raw_input(SD.Prompt2)#Check Input

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
else:
    print("Restart?")
    restart = raw_input("y/n:")
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

var1 = raw_input(SD.var1text)
var2 = raw_input(SD.var2text) 
SD.msg

#Get Email Ready
body1 = (SD.beforeIPText + " " + IP + " " + SD.afterIPText + "\r\n \r\n" + SD.var1text + var1 + "\r\n" + SD.var2text + var2 + "\r\n")
SD.msg.attach(MIMEText(body1, 'plain'))
#Connect & login to email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print("Logging In..")
server.login(SD.fromaddr, SD.password)
text = SD.msg.as_string()
print("Sending Email...")
server.sendmail(SD.fromaddr,email.rcpt,text)
server.quit()
#Email Done

# Log Notice
naive_dt = datetime.now() #set datetime to local timezone
print ("Logging to file at: ")
print(datetime.now().strftime("%a, %d %B %Y %I:%M"))
time.sleep(1)

# Storage & info for Log File
newline = ["\n"]  # b/c formating ;-)
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
print ("Device: " + IP + " Added to log & emailed IP" )
print ('Done')
time.sleep(5)
sys.exit()