import examModule as em

while(True):
	choice = int(input("Enter your choice :"))

	if(choice == 1):
		fact = em.findFactorial(int(input("Enter a number :")))
		print("sum of factorial is :"+str(fact))
	elif(choice == 2):
		data = em.findMultiplies(int(input("Enter a number :")))
		print(data)
	elif(choice == 3):
		arm = em.armStrongNumber(int(input("Enter no1 :")),int(input("Enter no2 :")))
	elif(choice == 4):
		fib = em.fibonacci()
		print(fib)
	elif(choice == 5):
		fac = em.primeMain(int(input("Enter no1 :")))	
	elif(choice == 6):
		div = em.divisible(2025)
	elif(choice == 7):
		sq1 = em.squareOfNumber(int(input("Enter number :")),int(input("Enter number :")))
		print(sq1)	
	elif(choice == 8):
		hip = em.highestPrime(int(input("Enter number :")),int(input("Enter number :")))
	elif(choice == 9):
		sq = em.sumOfSquare(int(input("Enter a number :")))
		print(sq)
	else:
		print("Bye")
		exit()