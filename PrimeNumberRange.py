#primeNumber range()
num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))
flag = False
for x in range(num1,(num2+1)):
	for y in range(2,(x//2) + 1):
		if(x%y == 0):
			break
		else:
			flag = True
	if(flag == True):
		print("Number is prime:"+str(x))
		flag = False

