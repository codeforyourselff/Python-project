#File handling program with read and write()
class Student():
	def addStudent(self):
		self.rollNo = int(input("Enter your rollNo :"))
		self.name = input("Enter your name:")
		self.city = input("Enter your city:")

	def writeStudent(self):
		self.data = open("Final_data.txt","a")
		self.data.write(str(self.rollNo) + " " + self.name + " " + self.city + ",")	
		self.data.close()

	def readDataStudent(self):
		self.data = open("Final_data.txt","r")
		return (self.data.read().split(","))
		self.data.close()	
		
	def searchData(self):
		self.searchData = input("Enter your search data:")
		for x in self.readDataStudent():
			self.data = x.split(" ")
			for y in range(len(self.data)):
				if(self.data[y] == self.searchData):
					print(self.data)

class Main():
	def mainMethod(self):
		print("---------------------------------------")
		print("Press 1 for add student into file")
		print("Press 2 for display student from file")
		print("Press 3 for search student from file")
		print("---------------------------------------")

		self.choice = int(input("Enter your choice:"))

		if(self.choice == 1):
			self.stu = Student()
			self.stu.addStudent()
		elif(self.choice == 2):
			self.stu.writeStudent()
		elif(self.choice == 3):
			self.data = self.stu.readDataStudent()
			print(self.data)
		elif(self.choice == 4):
			self.stu.searchData()

#mainFunction calling
mainCalling = Main()
while(True):
	mainCalling.mainMethod()		


# 1. Add Student(EnrollNum, Name, marks of 5 subjects)
# 2. Display All students
# 3. Display result(input: EnrollNum)
# 4. Display subject wise failure student(input subject)
# 	1. OOP
# 	2. Python
# 	3. Daa
# 5. Display top 5 students
# 6. Display details of failure students
# 7. Exit	