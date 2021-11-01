#Gui,label,radio,varMode1,entry,button
import tkinter
stulst = []
class Car():
    def __init__(self):
        self.check1 = 0
        self.check2 = 0
        self.check3 = 0
        self.radio  = 0
    
    def radioLogic(self):
        if(varEngine.get() == 1):
            self.radio = "V8"
            return self.radio
        else:
            self.radio = "V12"    
            return self.radio

    def checkLogic(self):
        if(varMode1.get() == 1):
            self.check1 = "Auto"
        if(varMode2.get() == 1):
            self.check2 = "Normal"
        if(varMode3.get() == 1):
            self.check3 = "AI"  

    def addCar(self):
        self.file = open("carData.txt","a")
        self.checkLogic()
        self.file.write(str(txt1.get()) + " " + str(txt2.get()) + " " + str(txt3.get()) + " " + str(self.radioLogic()) + " " + str(self.check1) + " " + str(self.check2) + " " + str(self.check3)  + "\n")
        self.file.close()

    @staticmethod
    def searchCar():
        companyData = txt1.get()
        count = 0
        file = open("carData.txt","r")
        for x in file:
            data = x.split(" ")
            if(companyData ==  data[0]):
                count = count + 1
                print(x)
        file.close()    
        lbl6.config(text = count)       
        
    @staticmethod
    def deleteFromFile():
    	file = open("carData.txt","r");
    	for x in file:
    		stulst.append(x)
    	file.close()		

    	model = txt3.get()
    	for x in stulst:
    		if model in x:
    			del(x)
    	print(stulst)		




carData = Car()        

window = tkinter.Tk()
window.title("Car Regitration Form")
window.config(bg = "black")
window.geometry("700x500")

lbl1 = tkinter.Label(window,text = "Car Company name:")
lbl1.config(bg = "Red")
lbl1.pack()
txt1 = tkinter.Entry()
txt1.pack()

lbl2 = tkinter.Label(window,text = "Car name:")
lbl2.config(bg = "Red")
lbl2.pack()
txt2 = tkinter.Entry()
txt2.pack()

lbl3 = tkinter.Label(window,text = "Car model number:")
lbl3.config(bg = "Red")
lbl3.pack()
txt3 = tkinter.Entry()
txt3.pack()

lbl4 = tkinter.Label(window,text = "Car engine type:")
lbl4.config(bg = "Red")
lbl4.pack()

varEngine = tkinter.IntVar()
radio1 = tkinter.Radiobutton(window,text = "V8",value = 1,variable = varEngine)
radio1.pack()
radio2 = tkinter.Radiobutton(window,text = "V12",value = 0, variable = varEngine)
radio2.pack()

lbl5 = tkinter.Label(window,text = "Car mode specification:")
lbl5.config(bg = "Red")
lbl5.pack()

varMode1 = tkinter.IntVar()
varMode2 = tkinter.IntVar()
varMode3 = tkinter.IntVar()

checkbox1 = tkinter.Checkbutton(window,text = "Auto",variable = varMode1)
checkbox1.pack()
checkbox2 = tkinter.Checkbutton(window,text = "Normal",variable = varMode2)
checkbox2.pack()
checkbox3 = tkinter.Checkbutton(window,text = "AI",variable = varMode3)
checkbox3.pack()

btn1 = tkinter.Button(window,text = "Add Car",command = carData.addCar)
btn1.config(bg = "yellow")
btn1.pack()

lbl6 = tkinter.Label(window,text = "This is default label")
lbl6.config(bg = "red")
lbl6.pack()

btn2 = tkinter.Button(window,text = "SearchCar",command = Car.searchCar)
btn2.config(bg = "yellow")
btn2.pack()

btn3 = tkinter.Button(window,text = "delete from file",command = Car.deleteFromFile)
btn3.config(bg = "yellow")
btn3.pack()

window.mainloop()
