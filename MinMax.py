# Min and Maximum fron three numbers:

number1 = int(input("Enter 1st Number:"))
number2 = int(input("Enter 2nd number:"))
number3 = int(input("Enter 3rd number:"))

if(number1 > number2 and number1 > number3):
	print("Number1 is maximum")
elif(number2 > number3 and number2 > number1):
	print("Number2 is maximum")
else:
	print("Number3 is maximum")	

if(number1 < number2 and number1 < number3):
	print("Number1 is minimum")
elif(number2 < number3 and number2 < number1):
	print("Number2 is minimum")
else:
	print("Number3 is minimum")			