#Stored Data.py v3.1
#For use with IP-Email.py (v3.1)
#Get at https://github.com/Protocol73
#Setting start at line 30 
import os
import time
import address as email
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

fromaddr = "your-email@gmail.com" #Your Gmail Address

# v v v WARNING v v v
password = "password123" #Gmail Password <--- WARNING THIS IS NOT Secure! BE CAREFUL ! YOU WERE WARNED !
# ^ ^ ^ WARNING ^ ^ ^

subject = "Test IP-Email Script" #change me

Prompt1 = ("IP of Device:")
Prompt2 = ("Enter IP Again:")

#var1 & 2 are used in the Prompt & the Email 
var1text = "Info Prompt 1:" #change me
var2text = "Info Prompt 2:" #change me

beforeIPText = "Installed:" #change me
afterIPText = "Static Stage/info Complete Text" #change me

msg = MIMEMultipart()
msg['subject'] = subject
msg['cc'] = email.cc
msg['to'] = email.to