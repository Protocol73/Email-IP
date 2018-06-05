#Stored Data.py
#For use with IP-Email.py
#Get at https://github.com/Protocol73

from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart

fromaddr = "example@gmail.com" #Your Gmail Address

# v v v WARNING v v v
password = "Password" #Gmail Password <--- WARNING THIS IS NOT SAFE! BE CAREFUL ! YOU WERE WARNED !
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