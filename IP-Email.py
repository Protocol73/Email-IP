import os
import time
import smtplib
import StoredData as SD
from email import encoders
from datetime import datetime
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart

#Begin Local Storage
msg = MIMEMultipart()
msg['Subject'] = "CHANGE ME"  # Email Subject
#End local Storage

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#This Block checks for valid looking IP address.
def validate_ip(s): 
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False #What did you type?
    return True # Looks Good

cls() #clear the Screen
SD.IP
SD.var1
SD.var2
cls() #again

if validate_ip(SD.IP) == True:
    print ("Accepted IP: " + SD.IP)
    time.sleep(1.5)
else:
    print("Error: Was that an IP address?")
    time.sleep(5)
    exit()
#Email Send 
msg.attach(MIMEText(SD.body1, 'plain'))
msg.attach(MIMEText(SD.body2, 'plain'))
msg.attach(MIMEText(SD.body3, 'plain'))
msg.attach(MIMEText(SD.body4, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(SD.fromaddr, SD.password)
text = msg.as_string()
server.sendmail(SD.fromaddr,SD.toaddr,text)
server.quit()

# Log Data to File
naive_dt = datetime.now() #set datetime to local timezone
print ("Logging to file at: ")
print(datetime.now().strftime("%a, %d %B %Y %I:%M"))
print ("Device: " + SD.IP + " Added to log")
time.sleep(1)

# String Storage for Log File
newline = ["\n"]  # b/c formating ;-)
text_ip = [SD.IP]
text_install = ["Installed & Emailed out:"]
endtxt = [" ----- Device Divider ----- "]
# End Data Storage
# file name & how to open it.
fh = open("Install Log.txt", "a") #Change File Name to Whatever.
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
time.sleep(.5)
print ('Done')
time.sleep(.5)
fh.close
#all done