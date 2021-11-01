def getTotalFactors(num):#10
	flag = False
	for y in range(2,(num+1) //2 ):#5
		if(num%y == 0):#10//2 == 0
			break
		else:
			flag = True
	return flag		

def isPrime(num):#10
	totalFactors = getTotalFactors(num)#10
	if(totalFactors == True):
		return True
	else:
		return False

def primeNumberCalculations(num1,num2):#(10,20)
	for x in range(num1,num2+1):#(10,20)
		flag = isPrime(x) #10
		if(flag):
			print("Number is prime:"+str(x))
			flag = False


num1 = int(input("Enter num1 :"))#10
num2 = int(input("Enter num2 :"))#20
primeNumberCalculations(num1,num2)#(10,20)