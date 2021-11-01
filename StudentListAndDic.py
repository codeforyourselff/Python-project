#Student data stored inside list with dictonary
student = []

def addStudent():
	stuData = {"Enroll_no":input("Enter enroll no:"),"Name":input("Enter name:"),"Marks":{"Python":int(input("Enter python marks:")),"Java":int(input("Enter java marks:")),"Cc":int(input("Enter cc marks:")),"RDBMS":int(input("Enter rdbms marks:")),"Daa":int(input("Enter daa marks:"))}}
	student.append(stuData)

def displayStudent():
	for x in range(len(student)):
		print("\t\t Enroll_no is:"+str(student[x]["Enroll_no"]))
		print("\t\t Name :"+str(student[x]["Name"]))
		print("\t\t Marks:"+str(student[x]["Marks"]))
		print("------------------------------------------------------")

def totalOfMarks(x):
	return (student[x]["Marks"]["Python"] + student[x]["Marks"]["Java"] + student[x]["Marks"]["Cc"] + student[x]["Marks"]["RDBMS"] + student[x]["Marks"]["Daa"])

def totalPercnt(x):
	return (x / 5) 

def displayResult():			
	enrollData = input("Enter enroll no:")
	for x in range(len(student)):
		if(student[x]["Enroll_no"] == enrollData):
			sumOf = totalOfMarks(x)
			percnt = totalPercnt(sumOf)
			print("totalOfMarks of student "+str(student[x]["Name"] + " is :"+ str(sumOf)))
			print("totalPercnt  of student "+str(student[x]["Name"] + " is :"+ str(percnt)))		

def displayPassOrFail():
	flag = False
	sub = input("Enter name of subject to check :")
	for x in range(len(student)):
		if sub in student[x]["Marks"]:
			if(student[x]["Marks"][sub] < 40):
				print(student[x])
			else:
				print("Pass")
		else:
			print("Detail not found")			

def topFiveStudent():
	length = len(student)
	for x in range(0,length-1):
		for y in range(0,(length -x) -1):
			if(totalOfMarks(y) < totalOfMarks(y+1)):
				temp = student[y+1]
				student[y+1] = student[y]
				student[y] = temp
	displayStudent()

def main():
	print("------------------------------------------------------")
	print("Press 1 to add student")
	print("Press 2 to display all student")
	print("Press 3 to display result of student as per enroll no")
	print("Press 4 to display subject wise failure student record")
	print("Press 5 to display top 5 student")
	print("Press 6 to exit")
	print("------------------------------------------------------")

	choice = int(input("Enter your choice :"))
	if(choice == 1):
		addStudent()
	elif(choice == 2):
		displayStudent()
	elif(choice == 3):
		displayResult()
	elif(choice == 4):
		displayPassOrFail()
	elif(choice == 5):
		topFiveStudent()
	else:
		exit()

while(True):
	main()