#create mobile using dic and list
mobile = []

def addMobile():
	mobileData = {"Model_no":input("Enter Model no:"),"Price":int(input("Enter price:")),"Company":input("Enter company:"),"No_of_cam":int(input("Enter no of cam:"))}
	mobile.append(mobileData)

def removeMobile():
	model = input("Enter model no to remove mobile :")
	for x in range(len(mobile)):
		if(mobile[x]["Model_no"] == model):
			del(mobile[x])			
	print("-----------------------------------------------------------------")				

def displayAllMobile():
	for singleMobile in mobile:
		print(singleMobile)
	print("-----------------------------------------------------------------")			

def accordingToCams():
	camNo = int(input("Enter no of camera :"))
	for x in range(len(mobile)):
		if(mobile[x]["No_of_cam"] > camNo):
			print(mobile[x])
	print("-----------------------------------------------------------------")		

def accordingToPrice():
	priceOf = int(input("Enter price :"))
	for x in range(len(mobile)):
		if(mobile[x]["Price"] < priceOf):
			print(mobile[x])			
	print("-----------------------------------------------------------------")				

def main():
	while(True):	
		print("-----------------------------------------------------------------")		
		print("Press 1 to add mobile")
		print("Press 2 to remove mobile")
		print("Press 3 to display all mobile phones")
		print("Press 4 to display mobile phones less than 2 cams")
		print("Press 5 to display mobile phones less than inputed price")
		print("Press 6 to exit")
		choice = int(input("Enter your choice :"))
		if(choice == 1):
			addMobile()
		elif(choice == 2):
			removeMobile()
		elif(choice == 3):
			displayAllMobile()
		elif(choice == 4):
			accordingToCams()
		elif(choice == 5):
			accordingToPrice()
		elif(choice == 6):
			print("Bye")
			exit()
main()