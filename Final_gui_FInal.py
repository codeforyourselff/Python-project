import tkinter
class Main():
    def __init__(self):
        self.master = None
        self.lbl1 = None
        self.lbl2 = None
        self.lbl3 = None
        self.lbl4 = None
        self.txt1 = None
        self.txt2 = None
        self.txt3 = None
        self.txt4 = None
        self.radio = None
        self.check1 = None
        self.check2 = None
        self.check3 = None

    def guiComponents(self):  
        self.master = tkinter.Tk()
        self.master.title("Car registration data")
        self.master.config(bg = "black")
        self.master.geometry("700x500")

        self.lbl1 = tkinter.Label(self.master,text = "EnrollNo")
        self.lbl1.pack()
        self.txt1 = tkinter.Entry()
        self.txt1.pack()

        self.lbl2 = tkinter.Label(self.master,text = "Name of student")
        self.lbl2.pack()
        self.txt2 = tkinter.Entry()
        self.txt2.pack()

        self.radio = tkinter.IntVar()
        self.lbl3 = tkinter.Label(self.master,text = "Select your gender")
        self.lbl3.pack()
        self.txt3 = tkinter.Radiobutton(self.master,value = 1,text = "Male",variable = self.radio)
        self.txt3.pack()
        self.txt4 = tkinter.Radiobutton(self.master,value = 0,text = "Female",variable = self.radio)
        self.txt4.pack()

        self.check1 = tkinter.IntVar()
        self.check2 = tkinter.IntVar()
        self.check3 = tkinter.IntVar()

        self.lbl4 = tkinter.Label(self.master,text = "please tick your interest")
        self.lbl4.pack()
        self.check1 = tkinter.Checkbutton(self.master,text = "Python",variable = self.check1)
        self.check1.pack()
        self.check2 = tkinter.Checkbutton(self.master,text = "Java",variable = self.check2)
        self.check2.pack()
        self.check3 = tkinter.Checkbutton(self.master,text = "Daa",variable = self.check3)
        self.check3.pack()

        self.btn1 = tkinter.Button(self.master,text = "Add Student",command = Student)
        self.btn1.config(bg = "red")
        self.btn1.pack()
        self.master.mainloop()

class Student(Main):
    def __init__(self):
       super().__init__()
maindata = Main()  
maindata.guiComponents()     