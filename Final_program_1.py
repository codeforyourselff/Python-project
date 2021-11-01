#Final program with File,class,object,exception,constructor
stulst = []
class Student():
    def __init__(self):
        self.enrollNo = input("Enter your enrollNo:")
        self.name = input("Enter your name:")
        self.python = int(input("Enter your python marks:"))
        self.java = int(input("Enter your java marks:"))
        self.rdbms = int(input("Enter your rdbms marks:"))
        self.daa = int(input("Enter your daa marks:"))
        self.cs = int(input("Enter your cs marks:"))

    def writeIntoFile(self):   
        self.file = open("finalStu.txt","a")
        self.file.write(str(self.enrollNo) + " " + str(self.name) + " " + str(self.python)+ " " + str(self.java)+ " " + str(self.rdbms)+ " " + str(self.daa)+ " " + str(self.cs)+ "\n")
        self.file.close()

    @staticmethod
    def displayStudent():
        try:
            file = open("finalStu.txt","r")
            for x in file:
                print(x)
            file.close() 
        except FileNotFoundError:
            print("File not existed!!")

    @staticmethod
    def totalMarks(x):
        data = x.split(" ")
        return (int(data[2]) + int(data[3]) + int(data[4]) + int(data[5]) + int(data[6]))

    @staticmethod
    def totalPercnt(x):
        try:
            return (Student.totalMarks(x)) / 5
        except ArithmeticError:
            print("Exception occured..!! Divide by zero")

    @staticmethod
    def displayResult():
        try:
            file = open("finalStu.txt","r")
            for x in file:
                print(Student.totalMarks(x))
                print(Student.totalPercnt(x))
            file.close() 
        except FileNotFoundError:
            print("File not found..!! Exception generated")

    @staticmethod
    def searchByEnroll():
        enroll = input("Enter enroll no to search:")
        file = open("finalStu.txt","r")
        for x in file:
            data = x.split()
            if(data[0] == enroll):
                print(x)
        file.close()   
    @staticmethod
    def sortingLst():
        for x in range(0,len(stulst) - 1):
            for y in range(0,len(stulst) - 1 - x):
                if(stulst[y] < stulst[y+1]):
                    temp = stulst[y+1]
                    stulst[y+1] = stulst[y]
                    stulst[y] = temp

        for x in stulst:
            file = open("finalStu.txt","r")
            for y in file:
                if(Student.totalPercnt(y) == x):
                    print(Student.totalPercnt(y))
                    print(y)
        file.close()

    @staticmethod
    def sortByPercnt():
        file = open("finalStu.txt","r")
        for x in file:
            data = Student.totalPercnt(x)
            stulst.append(data)
        file.close()   
        Student.sortingLst()            

    @staticmethod
    def subjectByFailure():
        print("------------------")
        subject = input("Enter subject to check:")
        main = 0
        if(subject == "python"):
            main = 2
        elif(subject == "java"):
            main = 3
        elif(subject == "rdbms"):
            main = 4    
        elif(subject == "daa"):
            main = 5
        elif(subject == "cs"):
            main = 6 
        else:
            print("No subject found entred by you:")       

        file = open("finalStu.txt","r")
        for x in file:
            data = x.split()
            if(int(data[main]) < 35):
                print(x)
        file.close()         

class Main():
    def mainFunction(self):
        while(True):
            print("----------------------------------")
            print("Press 1 to add student details into file")
            print("Press 2 to display student details from file")
            print("Press 3 to display totalMarks and percnt and show pass and fail")
            print("Press 4 to search student as per enrollNo")
            print("Press 5 to sort student as per percnt")
            print("Press 6 to display student as per failure in subject")
            print("Press 7 to exit")
            print("----------------------------------")

            self.choice = int(input("Enter your choice:"))
            if(self.choice == 1):
                self.studata = Student() 
                self.studata.writeIntoFile()
            elif(self.choice == 2):
                Student.displayStudent()
            elif(self.choice == 3):
                Student.displayResult() 
            elif(self.choice == 4):
                Student.searchByEnroll()
            elif(self.choice == 5):
                Student.sortByPercnt()
            elif(self.choice == 6):
                Student.subjectByFailure()              
            else:
                exit()
                
mainData = Main()
mainData.mainFunction()


