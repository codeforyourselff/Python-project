def findArmStrongNumber(lenn,num,sumOf):
	no = num
	while(num != 0):
		rem = num % 10
		sumOf = sumOf + (rem ** lenn)
		num = num // 10
	if(no == sumOf):
		return True

def findingLength(num):
	lenn = len(str(num))
	number = findArmStrongNumber(lenn,num,sumOf = 0)
	return number

def armStrongCalculations(num1,num2):
	for x in range(num1,num2):
		rem = findingLength(x)
		if(rem):
			print("Number is armstrong:"+str(x))

armStrongCalculations(int(input("Enter num1 :")),int(input("Enter num2 :")))