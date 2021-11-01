class Student():
	no=0
	name="ABC"
	city="ahmedabad"
	def getData(self):
		self.no=int(input("Enter your num"))
		self.name=input("Enter your name")
		self.city=input("Enter your city")
	def printData(self):
		print("Num is:"+str(self.no))
		print("Name is:"+str(self.name))
		print("City is:"+str(self.city))
	def writeToFile(self):
		fileStu = open("stuData.txt","a")
		fileStu.write(str(self.no)+" "+self.name+" "+self.city+"\n")
		fileStu.close()


while(True):
	print("1. Add Student")
	print("2. Display all students")
	print("3. Search by name")
	print("4. Exit")
	choice = int(input("Enter your choice:"))
	if(choice==1):
		stuObj = Student()
		stuObj.getData()
		stuObj.writeToFile()
	elif(choice==2):
		fileStu = open("stuData.txt","r")
		print(fileStu.read())
		fileStu.close()
	elif(choice==3):
		print("Search by name")
		searchName = input("Enter the name to Search:")
		fileStu = open("stuData.txt","r")
		for singleLine in fileStu:
			listContents = singleLine.split()
			if(listContents[1]==searchName):
				print(singleLine)
		fileStu.close()
	else:
		exit()





