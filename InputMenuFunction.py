num1 = 0
num2 = 0
def oddEven():
	num1 = int(input("Enter a number:"))
	if(num1 % 2 == 0):
		print("Number is even:"+str(num1))
		print("-------------------------")
	else:
		print("Number is odd:"+str(num1))
		print("-------------------------")
		
def armStrong():
	num1 = int(input("Enter 1st number:"))		
	no = num1
	sumOf = 0
	while(num1 != 0):
		rem = num1%10
		sumOf = sumOf + (rem * rem * rem)
		num1 = num1//10
	if(no == sumOf):
		print("Number is armstronge:"+str(no))
		print("-------------------------")
	else:
		print("Number is not armstrong:"+str(no))
		print("-------------------------")

def primeNum():
	flag = False
	num1 = int(input("Enter a number:"))
	for x in range(2, (num1+1) // 2):
		if(num1%x == 0):
			break
		else:
			flag = True	
	if(flag == True):
		print("Number is prime:"+str(num1))
		print("-------------------------")
	else:
		print("Number is not prime:"+str(num1))
		print("-------------------------")	

def primeInRang():
	num1 = int(input("Enter 1st number:"))
	num2 = int(input("Enter 2nd number:"))
	prime = 0
	flag = False
	for x in range(num1,num2+1):
		for y in range(2,(x// 2) + 1):
			if(x%y == 0):
				break
			else:
				flag = True
				prime = x	
		if(flag == True):
			print("Prime Number is :"+str(prime))
			print("-------------------------")
			flag = False

def evenRang():
	num1 = int(input("Enter 1st number:"))
	num2 = int(input("Enter 2nd number:"))

	for x in range(num1,num2+1):
		if(x%2==0):
			print("Number is even:"+str(x))
			print("-------------------------")

def exitFunc():
	print("Exited")
	exit()

while(True):
	print("Press 1 Find odd and even")
	print("Press 2 Armstronge")
	print("Press 3 Prime num")
	print("Press 4 prime num range")
	print("Press 5 even range")
	print("Press 6 for exit")		
	print("-------------------------")

	choice = int(input("Enter your choice:"))
	if(choice == 1):
		oddEven()
	elif(choice == 2):
		armStrong()
	elif(choice == 3):
		primeNum()
	elif(choice == 4):
		primeInRang()
	elif(choice == 5):
		evenRang()
	else:
		exitFunc()
		

						



