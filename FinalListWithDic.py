stulst = []
class Student():
    def __init__(self):
        self.studic = {"enrollNo":input("Enter your enrollNo:"),"stuName":input("Enter your name:"),"Marks":{"Python":int(input("Enter python marks:")),"Java":int(input("Enter java marks:")),"Rdbms":int(input("Enter rdbms marks:")),"Daa":int(input("Enter daa marks:")),"Cs":int(input("Enter cs marks:"))}}
        stulst.append(self.studic)

    @staticmethod
    def displayAllStudent():
        for x in stulst:
            print(x)    

    @staticmethod
    def totalMarks(x):
        return (stulst[x]["Marks"]["Python"] + stulst[x]["Marks"]["Java"] + stulst[x]["Marks"]["Rdbms"] + stulst[x]["Marks"]["Daa"] + stulst[x]["Marks"]["Cs"])

    @staticmethod
    def totalPercnt(x):
        return (Student.totalMarks(x)) / 5

    @staticmethod
    def displayStudentResult():
        enroll = input("Enter your enrollNo:")
        for x in range(0,len(stulst)):
            if(stulst[x]["enrollNo"] == enroll):
                print("Total marks of student " + stulst[x]["stuName"] + " is "  + str(Student.totalMarks(x)))
                print("Total percnt of student " + stulst[x]["stuName"] + " is "  + str(Student.totalPercnt(x)))

    @staticmethod
    def displayStudentSubjectWise():
        for x in range(len(stulst)):
            if(stulst[x]["Marks"]["Python"] > 40 and stulst[x]["Marks"]["Java"] > 40 and stulst[x]["Marks"]["Rdbms"] > 40 and stulst[x]["Marks"]["Daa"] > 40 and stulst[x]["Marks"]["Cs"] > 40 ):
                print(str(stulst[x]["stuName"]) + " is " + " pass in every subject ")
            else:
                if(stulst[x]["Marks"]["Python"] < 35):
                    print(str(stulst[x]["stuName"]) + " is fail in python")
                elif(stulst[x]["Marks"]["Java"] < 35): 
                    print(str(stulst[x]["stuName"]) + " is fail in java")
                elif(stulst[x]["Marks"]["Rdbms"] < 35):      
                    print(str(stulst[x]["stuName"]) + " is fail in rdbms")
                elif(stulst[x]["Marks"]["Daa"] < 35):          
                    print(str(stulst[x]["stuName"]) + " is fail in daa")
                elif(stulst[x]["Marks"]["Cs"] < 35):              
                    print(str(stulst[x]["stuName"]) + " is fail in cs")

class Main():
    def mainFunction(self):
        print("------------------------------------------------------")
        print("Press 1 to add student")
        print("Press 2 to display all student")
        print("Press 3 to display result of student as per enroll no")
        print("Press 4 to display subject wise failure student record")
        print("Press 5 to display top 5 student")
        print("Press 6 to exit")
        print("------------------------------------------------------")

        self.choice = int(input("Enter your choice:"))
        print("------------------------------------------------------")

        if(self.choice == 1):
            studata = Student()
        elif(self.choice == 2):
            Student.displayAllStudent()  
        elif(self.choice == 3):
            Student.displayStudentResult()
        elif(self.choice == 4):
            Student.displayStudentSubjectWise()
        else:
            exit()


maindata = Main()
while(True):
    maindata.mainFunction()