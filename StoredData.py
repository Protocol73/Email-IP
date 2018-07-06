#Stored Data.py For use with IP-Email.py
#Get at https://github.com/Protocol73/Email-IP
import os
import time
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()  

def importcheck():
	cls()
	print ("Do NOT run this file Directly.")
	print ("Simply define your settings here,")
	print ("And run Email-IP.py Your settings will be imported.")
	time.sleep(10)
	exit()

if __name__ == '__main__':
	importcheck()

# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
# DO NOT Change anything above this Line.

#Setting v v v 
fromaddr = "example@gmail.com" #Your Gmail Address

# v v v WARNING v v v
password = "Password" #Gmail Password <--- WARNING THIS IS NOT SECURE! BE CAREFUL ! YOU WERE WARNED !
# ^ ^ ^ WARNING ^ ^ ^

to = "example@gmail.com" #Main recipient for this email.
cc = "example@gmail.com,example@gmail.com" #People to also Recieve the email

rcpt = cc.split(",") + [to]

msg = MIMEMultipart()
msg['Subject'] = "CHANGE ME"  # Email Subject
msg['cc'] = cc
msg['to'] = to

IP = raw_input("IP of Device:")
var1 = raw_input('Varable Request 1:') #set these to what you want here & down below
var2 = raw_input('Varable Request 2:') #set here for prompts & below for email text

body1 = ("Installed: " + IP + "\r\nAfter ip Text \r\n" + "\r\nVarable Text 1:" + var1 + "\r\nVarable Text 2:" + var2)

#Writen by Protocol73