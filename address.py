#address.py (v3.1)
#For use with IP-Email.py (v3.1)
#Get at https://github.com/Protocol73

to = "test@gmail.com" #Main recipient for this email.
cc = "someone@somewhere.net,no1@knowwhere.io" #Seperate addresses with a comma.

# DO NOT Change anything below this Line.
# v v v v v v v v v v v v v v v v v v v v

rcpt = cc.split(",") + [to]

import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()  

def importcheck():
	cls()
	print ("Do NOT run this file Directly.")
	print ("Simply define your recipients here,")
	print ("And run Email-IP.py Your recipients will be imported.")
	time.sleep(10)
	exit()

if __name__ == '__main__':
	importcheck()