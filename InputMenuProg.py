sumRem = 0
while(True):
	print("Press 1 to Even or odd")
	print("Press 2 to Armstronge")
	print("Press 3 to Prime num")
	print("Press 4 to Prime num range")
	print("Press 5 to exit")
	print("----------------------------")

	choice = int(input("Enter a choice:"))
	if(choice <= 3):
		num1 = int(input("Enter a number:"))
		if(choice == 1):
			if(num1%2==0):
				print("Number is even"+str(num1))
				print("------------------------")
			else:
				print("Number is odd:"+str(num1))
				print("------------------------")
		elif(choice == 2):
			num = num1
			while(num1 != 0):
				rem = num1%10	
				sumRem = sumRem + (rem * rem * rem)
				num1 = num1//10
			if(sumRem == num):
				print("Number is armstronge:")
				print("------------------------")
			else:
				print("Number is not armstronge:")	
				print("------------------------")
		elif(choice == 3):
			flag = False
			for x in range(2, (num1//2) + 1):
				if(num1%x == 0):
					break
				else:
					flag = True
			if(flag == True):
				print("Number is prime:")
				print("------------------------")
			else:
				print("Number is not prime:")	
				print("------------------------")					
	else:
		if(choice == 4):
			num1 = int(input("Enter number one:"))
			num2 = int(input("Enter number two:"))
			flag = False
			for x in range(num1,(num2 + 1)):
				for y in range(2, (x//2)+1):
					if(x%y == 0):
						break	
					else:
						flag = True	
				if(flag == True):
					print("Number is prime:"+str(x))
					print("------------------------")
					flag = False
		elif(choice == 5):
			num1 = int(input("Enter number one:"))
			num2 = int(input("Enter number two:"))
			for x in range(num1,(num2 + 1)):
				if(x%2 == 0):
					print("Number is even"+str(x))
				else:
					print("Number is odd:"+str(x))
			print("------------------------")
		elif(choice == 6):
			print("Chal kat le idhar se:")
			exit()								
