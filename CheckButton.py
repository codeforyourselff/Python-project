import tkinter

def actionBtn():
	if(varGender1.get() == 1):
		lbl.config(text = "Ahmedabad")
	if(varGender2.get() == 1):
		lbl.config(text = "Vadodara")
	if(varGender3.get() == 1):
		lbl.config(text = "Surat")
	if(varGender4.get() == 1):
		lbl.config(text = "Mumbai")

		# print("Ahmedabad")
		# lbl.config(text = "Ahmedabad")
	# elif(varGender.get() == 1):
	# 	print("Vadodara")
	# 	lbl.config(text = "Vadodara")
	# elif(varGender.get() == 2):
	# 	print("Surat")
	# 	lbl.config(text = "Surat")
	# elif(varGender.get() == 3):
	# 	print("Mumbai")	
	# 	lbl.config(text = "Mumbai")


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

varGender1 = tkinter.IntVar()
varGender2 = tkinter.IntVar()
varGender3 = tkinter.IntVar()
varGender4 = tkinter.IntVar()

lbl = tkinter.Label(window,text = "")
lbl.pack()

check1 = tkinter.Checkbutton(window,text = "Ahmedabad",variable = varGender1).pack()

check2 = tkinter.Checkbutton(window,text = "Vadodara",variable = varGender2).pack()

check3 = tkinter.Checkbutton(window,text = "Surat",variable = varGender3).pack()

check4 = tkinter.Checkbutton(window,text = "Mumbai",variable = varGender4).pack()

btn = tkinter.Button(window,text = "Click me..",command = actionBtn).pack()

window.mainloop()