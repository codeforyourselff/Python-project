#Stack using menu driven program
#size = int(input("Enter the size of list :"));
lst = [12,52,62,45,32,25,48,27,34,26,36]
def pushMethod():
	ele = int(input("Enter element to push into list :"))
	lst.append(ele)

def popMethod():
	print(len(lst))
	lst.pop(int(input("Enter element you want to remove :")))

def displayMethod():
	for x in lst:
		print(str(x))				

def stackUsingMenuDriven():
	while(True):
		print("---------------------------------")
		print("Press 1 for push element:")
		print("Press 2 for pop element:")
		print("Press 3 for display elements:")
		print("Press 4 for exit:")
		choice = int(input("Enter your choice :"))

		if(choice == 1):
			pushMethod()
		elif(choice == 2):
			popMethod()
		elif(choice == 3):
			displayMethod()
		else:
			print("Bye")
			exit()	

stackUsingMenuDriven()	