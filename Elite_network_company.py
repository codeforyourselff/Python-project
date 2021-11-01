#Elite_network_company program

print("\t\t\t 'Elite Network Company' \t\t\t\n")
print("\t 'Welcome to login screen!' \t\n")
print("Please enter your credentials:\n")

username=""
password=""

while not username and not password:
	username = input("Enter username:")
	password = input("Enter password:")	

	if username=="krishna" and password=="Krishna@123":
		print("Hey",username,"nice to meet you")
		print("security level=5")
	elif username=="rom" and password=="Rom@123":
		print("Hey",username,"you are late!")
		print("security leve=3")
	elif username=="madhur" and password=="Madhur@123":
		print("Hey",username,"Why are you haven't sign in:")
		print("security level = 2")
	else:
		print("Please enter your id & password")				

input("Press any key to exit...")