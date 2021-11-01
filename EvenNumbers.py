#EvenNumbers
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
print("-----------------------")

for x in range(num1,(num2+1)):
	if(x%2 == 0):
		print("Even number:"+str(x))	