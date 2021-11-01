studentList = []
class Student():
	def getData(self):
		self.studentDic = {"Enroll_no":input("Enter enroll no:"),"Name":input("Enter name:"),"python":int(input("Enter python marks:")),"java":int(input("Enter java marks:")),"rdbms":int(input("Enter rdbms marks:")),"daa":int(input("Enter daa marks:")),"cc":int(input("Enter cc marks:"))}
		studentList.append(self.studentDic)

	def printData(self):
		for x in range(len(studentList)):
			print(str(studentList[x]["Name"]) + " enroll no is " + str(studentList[x]["Enroll_no"]))
			print("Marks of python :"+str(studentList[x]["python"]))
			print("Marks of java :"+str(studentList[x]["java"]))
			print("Marks of rdbms :"+str(studentList[x]["rdbms"]))
			print("Marks of daa :"+str(studentList[x]["daa"]))
			print("Marks of cc :"+str(studentList[x]["cc"]))
			print("------------------------------------------------------")

	def totalMarks(self,x):
		print(str(studentList[x]["Name"]) + " enroll no is " + str(studentList[x]["Enroll_no"]))
		print("\tMarks of python :"+str(studentList[x]["python"]))
		print("\tMarks of java :"+str(studentList[x]["java"]))
		print("\tMarks of rdbms :"+str(studentList[x]["rdbms"]))
		print("\tMarks of daa :"+str(studentList[x]["daa"]))
		print("\tMarks of cc :"+str(studentList[x]["cc"]))
		return (studentList[x]["python"] + studentList[x]["java"] + studentList[x]["rdbms"] + studentList[x]["daa"] + studentList[x]["cc"])
		print("------------------------------------------------------")

	def totalPercnt(self,x):
		return	(x / 5);

	def resultData(self):
		self.enrollNo = input("Enter enrollNo to display result :")
		for x in range(len(studentList)):
			if(studentList[x]["Enroll_no"] == self.enrollNo):
				self.marks = self.totalMarks(x)
				self.percntage = self.totalPercnt(self.marks)
				print("Total marks of "+str(studentList[x]["Name"]) + " is " + str(self.marks))
				print("Total percnt of "+str(studentList[x]["Name"]) + " is " + str(self.percntage))
			else:
				print("Student not found")

	def subjectWiseFailureStudent(self):
		for x in range(len(studentList)):
			if((studentList[x]["python"] > 40) and (studentList[x]["java"] > 40) and (studentList[x]["rdbms"] > 40) and (studentList[x]["daa"] > 40) and (studentList[x]["cc"] > 40)):
				print(str(studentList[x]["Name"]) + " is pass in all subject")
			else:
				if(studentList[x]["python"] < 40):
					print(str(studentList[x]["Name"]) + " fail in python :" +str(studentList[x]["python"]))
				elif(studentList[x]["java"] < 40):
					print(str(studentList[x]["Name"]) + " fail in java :" +str(studentList[x]["java"]))
				elif(studentList[x]["rdbms"] < 40):
					print(str(studentList[x]["Name"]) + " fail in rdbms :" +str(studentList[x]["rdbms"]))
				elif(studentList[x]["daa"] < 40):
					print(str(studentList[x]["Name"]) + " fail in daa :" +str(studentList[x]["daa"]))
				elif(studentList[x]["cc"] < 40):	
					print(str(studentList[x]["Name"]) + " fail in cc :" +str(studentList[x]["cc"]))

	def displayTopFiveStudent(self):
		for x in range(0,len(studentList) - 1):
			for y in range(0,len(studentList) - x - 1):
				if(self.totalMarks(y) < self.totalMarks(y+1)):				
					self.temp = studentList[y]
					studentList[y] = studentList[y+1]
					studentList[y+1] = self.temp
		print("\t",studentList)			
		
class Main():
	while(True):
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
			stuData = Student()
			stuData.getData()
		elif(choice == 2):
			stuData.printData()
		elif(choice == 3):
			stuData.resultData()		
		elif(choice == 4):
			stuData.subjectWiseFailureStudent()
		elif(choice == 5):
			stuData.displayTopFiveStudent()
		else:
			exit()

mainData = Main()		