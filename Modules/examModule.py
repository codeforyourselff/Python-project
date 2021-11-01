def findSumOfFactors(num,sumOf):
	no = num
	while(num != 0):
		rem = num % 10
		sumOf = sumOf + rem
		num = num // 10
	return sumOf
		
def findFactorial(num):
	fact = 1
	temp = 0
	for x in range(num,0,-1):
		fact = fact * x
	return findSumOfFactors(fact,sumOf = 0)	

def findMultiplies(num):
	sumOf = 0
	for x in range(1,num):
		if((x %3 == 0) or (x % 5 == 0)):
			sumOf = sumOf + x
	return sumOf		

def armStrongNumberCal(length,num,sumOf):
	no = num
	while(num != 0):
		rem = num % 10
		sumOf = sumOf + (rem ** length)
		num = num // 10
	if(no == sumOf):
		return True

def armStrongNumberLen(num):
	length = len(str(num))
	sumOf = 0
	return armStrongNumberCal(length,num,sumOf = 0)

def armStrongNumber(num1,num2):
	for x in range(num1,num2+1):
		data = armStrongNumberLen(x)
		if(data):
			print("Number is armstrong :"+str(x))

def fibonacciCalculations(num1,num2,num3,count,sumOf):
	while(count != 18):
		num3 = num1 + num2
		if(num3 %2 == 0):
			sumOf = sumOf + num3	
		temp = num2
		num2 = num3
		num1 = temp
		count = count + 1
	return sumOf

def fibonacci():
	num1 = num3 = 0
	num2 = 1
	data = fibonacciCalculations(num1,num2,num3,count = 0,sumOf = 0)
	return data

def totalPrimeFactors(x,num,temp):
	flag = False
	for y in range(2,x+1):
		if(x%y==0):
			break
		else:
			flag = True
	if(flag == True):
		temp = x
		flag = False		
		print("largest Prime factors:"+str(temp))		

def primeFactors(x,num):
	if(num%x==0):
		totalPrimeFactors(x,num,temp = 0)

def primeMain(num):
	for x in range(1,num+1):
		primeFactors(x,num)		

def divisible():
	num = 2520
	if((num%1==0 and num%2==0 and num%3==0 and num%4==0 and num%5==0 and num%6==0 and num%7==0 and num%8==0 and num%9==0 and num%10==0) and (num%11==0 and num%12==0 and num%13==0 and num%14==0 and num%15==0 and num%16==0 and num%17==0 and num%18==0 and num%19==0 and num%20==0)):
		print(2520)

def totalSquareNumbers(num1,num2,sumOf):
	for x in range(num1,num2 + 1):
		sumOf = sumOf + x
	return sumOf ** 2


def squareOfNumber(num1,num2):
	sumOf = 0
	for x in range(num1,num2 + 1):
		sumOf = sumOf + (x ** 2)
	data = totalSquareNumbers(num1,num2,sumOf = 0)	
	return (data - sumOf)

def highestPrime(num1,num2):
	temp = 0
	flag = False
	count = 0
	for x in range(num1,num2 + 1):
		for y in range(2, (x + 1)):
			if(x%y==0):
				break
			else:
				flag = True;
		if(flag == True):
			count = count + 1
			temp = x
			flag = False
			#print("prime number:"+str(temp))
	print("At "+str(count)+" prime number is:"+str(temp))				

def sumOfDigits(num,temp,sumOf):
	while(num != 0):
		rem = num % 10
		sumOf = sumOf + rem
		num = num // 10
	return sumOf
		
def sumOfSquare(num):
	squareOfNumber = (2 ** num)
	temp = 0
	data = sumOfDigits(squareOfNumber,temp,sumOf = 0)
	return data




	


