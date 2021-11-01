#Marksheet analysis tool
lst = []

def addMarks():
	for x in range(0,7):
		ele = int(input("Enter marks :"))
		lst.append(ele)

def removeMarks():
	lst.remove(int(input("Enter element to remove from list :")))
	print("Element is removed")	

def displayTopFiveCalculations(lst,y,temp):
	if(lst[y] < lst[y+1]):
		temp = lst[y+1]
		lst[y+1] = lst[y]
		lst[y] = temp

def displayTopFive():
	length = len(lst) - 1;
	temp = 0
	for x in range(0,length-1):
		for y in range(0,(length -1) - x):
			 displayTopFiveCalculations(lst,y,temp)
	print(lst)			

def displaySecondHighest():
	print("The second highest marks :"+str(lst[1]))

def lessThanInputedMarks():
	inputMarks = int(input("Enter marks to check :"))
	for x in lst:
		if(x < inputMarks):
			print("Marks that are lesser than inputed marks :"+str(x))

def greaterThanInputedMarks():
	inputMarks = int(input("Enter marks to check :"))
	for x in lst:
		if(x > inputMarks):
			print("Marks that are greater than inputed marks :"+str(x))			

def mainFunction():
	while(True):

		print("---------------------------------")
		print("Press 1 for add marks :")
		print("Press 2 for remove marks :")
		print("Press 3 for display top 5 marks ")
		print("Press 4 for display 2nd highest mark:")
		print("Press 5 for display less than inputed mark:")
		print("Press 6 for display more than inputed mark:")
		print("Exit")

		choice = int(input("Enter your choice :"))
		if(choice == 1):
			addMarks()
		elif(choice == 2):
			removeMarks()
		elif(choice == 3):
			data = displayTopFive()
		elif(choice == 4):
			displaySecondHighest()
		elif(choice == 5):
			lessThanInputedMarks()
		elif(choice == 6):
			greaterThanInputedMarks()
		else:
			exit()

mainFunction()	

