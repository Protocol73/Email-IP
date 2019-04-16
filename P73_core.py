#Defaut import for Programs writen by Protocol73
#P73_core.py Subject to Change Without Notice
# --- V 0.0.1 --- Feb 2018  

import os
import sys
import time

def clear_term(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
clear_term() 

def Check_Prompt():#For Asking the User Yes or No answers
	input_answer = input("Yes/No:")
	answer = input_answer.lower()
	if answer in ['n','no']:
		return False
	elif answer in ['y','yes']:
		return True
	else:
		print("Error: Expected Yes or No, Got:" + input_answer)
		time.sleep(2)
		clear_term()
		return -1

def end_of_job():#quits the Program
	print("Are you sure you want to quit?")
	if Check_Prompt() is True:
		clear_term()
		sys.exit()
	else:
		print("Restarting Program")
		time.sleep(1)
		os.execl(sys.executable, sys.executable, *sys.argv)