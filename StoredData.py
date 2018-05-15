#Stored Data.py
#For use with IP-Email.py
#Get at https://github.com/Protocol73
# v v v WARNING v v v
password = "Password" #Gmail Password <--- WARNING THIS IS NOT SAFE! BE CAREFUL ! YOU WERE WARNED !
# ^ ^ ^ WARNING ^ ^ ^

IP = raw_input("IP of Device:")
var1 = raw_input('Varable Request 1:') #set these to what you want
var2 = raw_input('Varable Request 2:')

fromaddr = "example@gmail.com" #Your Gmail Address
toaddr = "example@gmail.com","example@gmail.com" #People to Recieve the email

body1 = ('Completed: ' + IP)
body2 = (" Please Configure Device")
body3 = (" custom Var1:" + var1) #Set these to what you want.
body4 = (" custom Var2:" + var2) #And leave that Space There... 

