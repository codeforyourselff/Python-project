#Final gui prog contains class,object,gui and file
#Objective
#1. Student details from gui // Enroll_no,name,marks of 5 subj
#2. Create object of student
#3. display the details of student

import tkinter as gui

def studentData():
	file = open("Gui.txt","a")
	file.write(str(txtField1.get()) + " " + str(txtField2.get()) + " " + str(txtField3.get()) + " " + str(txtField4.get()) + " " + str(txtField5.get()) + " " + str(txtField6.get()) + " " + str(txtField7.get()) + "\n")
	file.close()	

def displayStudent():
	file = open("Gui.txt","r")
	print(file.read())
	file.close()	

def totalMarks(x):
	lst = [x]
	for x in lst:
		print(x.split(" "))

def displayStudentByEnrollNo():
	enroll = txtField8.get()
	file = open("Gui.txt","r")
	stud = file.read().split("\n")
	for x in stud:
		if enroll in x:
			print(x)
			print(totalMarks(x))
	file.close()		




window = gui.Tk()
window.title("Student details")
window.config(bg ="black")
window.geometry("700x700")

lbl1 = gui.Label(window,text = "Enter enroll no").pack()
txtField1 = gui.Entry(window)
txtField1.pack()

lbl2 = gui.Label(window,text = "Enter name").pack()
txtField2 = gui.Entry(window)
txtField2.pack()

lbl3 = gui.Label(window,text = "Python").pack()
txtField3 = gui.Entry(window)
txtField3.pack()

lbl4 = gui.Label(window,text = "Java").pack()
txtField4 = gui.Entry(window)
txtField4.pack()

lbl5 = gui.Label(window,text = "Rdbms").pack()
txtField5 = gui.Entry(window)
txtField5.pack()

lbl6 = gui.Label(window,text = "Daa").pack()
txtField6 = gui.Entry(window)
txtField6.pack()

lbl7 = gui.Label(window,text = "Cc").pack()
txtField7 = gui.Entry(window)
txtField7.pack()

btn1 = gui.Button(window,text = "Enter data into",command = studentData)
btn1.pack()

btn2 = gui.Button(window,text = "Display Student",command = displayStudent)
btn2.pack()

btn3 = gui.Button(window,text = "Display Student By EnrollNo",command = displayStudentByEnrollNo)
btn3.pack()

lbl8 = gui.Label(window,text = "Enter enrollNo to check result:").pack()
txtField8 = gui.Entry(window)
txtField8.pack()

window.mainloop()

