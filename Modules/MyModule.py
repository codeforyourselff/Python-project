def oddEven(num):
	if(num%2==0):
		return True
	else:
		return False

def armStrong(num,sumOf = 0):
	no = num
	length = len(str(num))
	while(num != 0):
		rem = num % 10
		sumOf = sumOf + (rem ** length)
		num = num // 10
	if(no == sumOf):
		return True
	else:
		return False

def isPrime(num):
	flag = False
	for x in range(2, (num//2) + 1):
		if(num%x == 0):
			break
		else:
			flag = True	
	if(flag == True):
		return True
	else:
		return False

def getTotalFactors(num,flag):
	for y in range(2,(num+1) //2 ):
		if(num%y == 0):
			break
		else:
			flag = True
	return flag		

def isPrime(num):
	totalFactors = getTotalFactors(num,False)
	if(totalFactors == True):
		return True
	else:
		return False

def primeNumberCalculations(num1,num2):
	for x in range(num1,num2+1):
		flag = isPrime(x) 
		if(flag):
			print("Number is prime:"+str(x))
			flag = False	

def oddEvenRangeLogic(x):
	if(x%2==0):
		return "Number is even:"+str(x)
	else:
		return "Number is odd:"+str(x)

def oddEvenRange(num1,num2):
	for x in range(num1,(num2) + 1):
		isOddEven = oddEvenRangeLogic(x)
		print(isOddEven)
				

