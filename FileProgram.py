#File demo program with file handling
class Student():
	def addStudent(self):
		self.enrollNo = input("Enter you enrollNo:")
		self.name = input("Enter your name:")
		self.python = int(input("Enter your python marks:"))
		self.java = int(input("Enter your java marks:"))
		self.rdbms = int(input("Enter your rdbms marks:"))
		self.daa = int(input("Enter your daa marks:"))
		self.cc = int(input("Enter your cc marks:"))

	def writeIntoFile(self):
		self.file = open("student.txt","a")
		self.file.write(str(self.enrollNo) + " " + str(self.name) + " " + str(self.python) + " " + str(self.java) + " " + str(self.rdbms) + " " + str(self.daa) + " " + str(self.cc) + " \n")
		self.file.close()

	def readIntoFile(self):
		self.file = open("student.txt","r")
		print(self.file.read())
		self.file.close()

	def displayResult(self):
		self.ele = input("Enter enrollNo:")
		self.file = open("student.txt","r")
		self.data = self.file.read().split("\n")
		for x in self.data:
			if(self.ele in x):
				print(x)


	def displayStuAsResult(self):
		self.ele = int(input("Enter subject to check failure student:"))
		self.file = open("student.txt","r")
		for x in self.file.read().split("\n"):
			for y in x.split(" "):
				print(y)
				
			


class MainDemo():
	while(True):
		print("---------------------------------------------")
		print("Press 1 to add student:")
		print("Press 2 to display student:")
		print("Press 3 to display result:")
		print("Press 4 to display student as per failure in sub:")
		print("Press 5 to top 5 students:")
		print("Press 6 to display details fo faliure student:")
		print("---------------------------------------------")

		choice = int(input("Enter your choice:"))
		print("---------------------------------------------")

		if(choice == 1):
			stu = Student()
			stu.addStudent()
			stu.writeIntoFile()
		elif(choice == 2):	
			stu.readIntoFile()
		elif(choice == 3):
			stu.displayResult()
		elif(choice == 4):
			stu.displayStuAsResult()

maindata = MainDemo()
