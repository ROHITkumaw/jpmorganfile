import os 
import getpass                      
os.system("tput setaf 5")
print("\t\t\tWelcome to the World of TUI\t\t\t")
os.system("tput setaf 7")
print("\t\t\t----------------------------")
passwd = getpass.getpass("Enter your password:")
apass = "redhat"
if passwd != apass:
	print("Incorrect autentication") 
	exit()
print("Where you would like to perform your job(local/remotely) :", end = '')
location = input()
print(location)
if location == "remotely":
	     remoteIP = input("Enter your ipaddress :")
while True: 

	print("""press 1:To see Date Command 
	press 2:To see Cal Command 
	press 3:To Configure Web Server 
	press 4:To Create user name
	press 5:To Delete user name
	press 6:Check what you had copy just now 
	press 7:Exit
	"""
	)

	print("Enter your choice:", end='')  
	ch = input()
	print(ch);

	if location == "local":
	  if int(ch) == 1: 
		     os.system(" date")
	  elif int(ch) == 2: 
		     os.system("cal")
	  elif int(ch) == 3: 
		     os.system("yum install httpd")
	  elif int(ch) == 4: 
		    print("Enter the username you want to add: ", end = '')
		    Create_user = input()
		    os.system("useradd {}".format(Create_user))
	  elif int(ch) == 5: 
		   print("Enter the username you want to delete: ", end = '')
		   Create_user = input()
		   os.system("userdel -r {}".format(Create_user))                 
	  elif int(ch) == 6: 
		   os.system("xclip -o")  
	  elif int(ch) == 7: 
		   exit()                        
	  else:
		  print("Option not Supported")
	  input("Press enter to continue.......")
	  os.system("clear")
	  
	elif location == "remotely": 
	  if int(ch) == 1: 
		     os.system("ssh {} date".format(remoteIP))
	  elif int(ch) == 2: 
		     os.system("ssh {} cal".format(remoteIP))
	  elif int(ch) == 3: 
		     os.system("date")
	  elif int(ch) == 4: 
		    print("Enter the username you want to add: ", end = '')
		    Create_user = input()
		    os.system("ssh {0} useradd {1}".format(remoteIP,Create_user))
	  elif int(ch) == 5: 
		   print("Enter the username you want to delete: ", end = '')
		   Create_user = input()
		   os.system("ssh 192.168.1.102 userdel -r {}".format(Create_user))
	  elif int(ch) == 6: 
		   os.system("xclip -o")
	  elif int(ch) == 7: 
		   os.system("date")
	  else:
	       print("Location not found !")   
	  input("Press enter to continue.......")
	  os.system("clear") 




