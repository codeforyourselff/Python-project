#All three cases using switch case:
#Prime Number logic
def prime():
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
	print("-------------------------------")					
#ArmStrong number logic
def armStrong():
	num1 = int(input("Enter a num1:"))
	num2 = int(input("Enter a num2:"))
	sumOf = 0
	rem = 0

	for x in range(num1,(num2 +1)):
		no = x
		if(x <= 99):
			while(x > 0):
				rem = x%10
				sumOf = sumOf + (rem * rem)
				x = x//10
			if(sumOf == no):
				print("No is ArmStrong:"+str(no))
			sumOf = 0	
		else:
			while(x > 0):
				rem = x%10
				sumOf = sumOf + (rem *rem * rem)
				x = x//10
			if(sumOf == no):
				print("No is ArmStrong:"+str(no))
			sumOf = 0	
	print("-------------------------------")
#even number logic					
print("Even number:")
def even():
	num1 = int(input("Enter number1:"))
	num2 = int(input("Enter number2:"))

	for x in range(num1,num2+1):
		if(x%2 == 0):
			print("Even number:"+str(x))			
def AllThreeFunctions(x):
	switcher = {

		1 : prime(),
		2 : armStrong(),
		3 : even(),
	}

print("Press 1 for prime numbers")
print("Press 2 for armstrong numbers")
print("Press 3 for even numbers")
print("-------------------------")
AllThreeFunctions(int(input("Enter a choice:")))	