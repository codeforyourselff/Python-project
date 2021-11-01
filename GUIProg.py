import tkinter

def actionBtn():
	if(varGender.get() == 0):
		print("Ahmedabad")
		lbl.config(text = "Ahmedabad")
	elif(varGender.get() == 1):
		print("Vadodara")
		lbl.config(text = "Vadodara")
	elif(varGender.get() == 2):
		print("Surat")
		lbl.config(text = "Surat")
	elif(varGender.get() == 3):
		print("Mumbai")	
		lbl.config(text = "Mumbai")


window = tkinter.Tk()
window.title("My First GUI")
window.config(bg = "black")
window.geometry("800x500")

# lbl1 = tkinter.Label(window,text = "This is first label")
# lbl1.pack()

# lbl2 = tkinter.Label(window,text = "This is second label")
# lbl2.pack()

# btn = tkinter.Button(window,text = "Submit")
# btn.pack()

varGender = tkinter.IntVar()
print(varGender)

lbl = tkinter.Label(window,text = "This is default label")
lbl.pack()

radioCity1 = tkinter.Radiobutton(window,text = "Ahmedabad",value = 0,variable = varGender)
radioCity1.pack()

radioCity2 = tkinter.Radiobutton(window,text = "Vadodara",value = 1,variable = varGender)
radioCity2.pack()

radioCity3 = tkinter.Radiobutton(window,text = "Surat",value = 2,variable = varGender)
radioCity3.pack()

radioCity4 = tkinter.Radiobutton(window,text = "Mumbai",value = 3,variable = varGender)
radioCity4.pack()

btn = tkinter.Button(window,text = "Click me..",command = actionBtn)
btn.pack()




window.mainloop()