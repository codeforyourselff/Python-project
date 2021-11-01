import MyModule as ks

while(True):

	print("--------------------------------------")
	print("Press 1 to check odd and even")
	print("Press 2 to check armstrong")
	print("Press 3 to check prime")
	print("Press 4 to check prime number in range")
	print("Press 5 to check odd and even in range")
	print("Press 6 for exit")

	choice = int(input("Enter your choice :"))
	if(choice == 1):
		isOddEven = ks.oddEven(int(input("Enter the number to check odd & even :")))
		print(isOddEven)
	elif(choice == 2):
		isArmStrong = ks.armStrong(int(input("Enter the number to check armstrong :")))
		print(isArmStrong)
	elif(choice == 3):
		isPrime = ks.isPrime(int(input("Enter the number to check prime:")))
		print(isPrime)	
	elif(choice == 4):
		ks.primeNumberCalculations(int(input("Enter the number to check prime:")),int(input("Enter the number to check prime:")))
	elif(choice == 5):
		ks.oddEvenRange(int(input("Enter the number to odd and even:")),int(input("Enter the number to odd and even:")))
	elif(choice == 6):
		print("Bye")
		exit(0)