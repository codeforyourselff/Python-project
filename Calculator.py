#calculator prog
import tkinter as tk
value = []

class functionsData():
	def addValues(self):
		self.vals = self.txtField.get()
		self.value.append(vals)	

	def findMax(self):
		self.maxGuess = value[0]
		for x in self.value:
			if(x > self.maxGuess):
				self.maxGuess = x
		print(self.maxGuess)		


class Gui():
	def mainFunction(self):
		self.window = tk.Tk()
		self.window.title("Simple calculator")
		self.window.config(bg="black")
		self.window.geometry("800x500")

		self.lbl = tk.Label(self.window,text = "Enter values into box:")
		self.lbl.pack()

		self.txtField = tk.Entry(self.window)
		self.txtField.pack()

		self.btn1 = tk.Button(self.window,text = "Add",command = functionsData().addValues)
		self.btn1.pack()

		self.btn2 = tk.Button(self.window,text = "Max",command = functionsData().findMax)
		self.btn2.pack()

		self.window.mainloop()

guiData = Gui()	
guiData.mainFunction()