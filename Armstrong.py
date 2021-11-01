#ArmStrong progran
num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))
count = 0
sumOf = 0
rem = 0

for x in range(num1,(num2+1)):
	no = x
	if(x <= 99):
		while x > 0:
			rem = x%10
			sumOf = sumOf + (rem * rem)
			x = x//10
		if(no == sumOf):
			print("Number is armstrong:" + str(no))	
		sumOf = 0	
	else:
		while x > 0:
			rem = x%10
			sumOf = sumOf + (rem * rem * rem)
			x = x//10
		if(no == sumOf):
			print("Number is armstrong:"+ str(no))				
		sumOf = 0	