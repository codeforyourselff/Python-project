import random

list = [1,2,3,4,5,6,7,8,9,10,'A','K','Q','J']
count = 0
sumOf_1 = 0
sumOf_2 = 0
roundOf = 0

def declareWinnerCalculations1(user_1,user_2,user1Amount,user2Amount,user_1_bet,user_2_bet):
	user2Amount = user2Amount - user_2_bet
	user1Amount = user1Amount + user_2_bet
	print(str(user_2)+" lose :"+str(user_2_bet) + " amount")
	print("total amount have by " + str(user_2) + " is " + str(user2Amount))
	print("total amount have by " + str(user_1) + " is " + str(user1Amount))
	return [user1Amount,user2Amount]

def declareWinnerCalculations2(user_1,user_2,user1Amount,user2Amount,user_1_bet,user_2_bet):
	user1Amount = user1Amount - user_1_bet	
	user2Amount = user2Amount + user_1_bet
	print(str(user_1)+" lose :"+str(user_1_bet) + " amount")
	print("total amount have by " + str(user_1) + " is " + str(user1Amount))
	print("total amount have by " + str(user_2) + " is " + str(user2Amount))
	return [user1Amount,user2Amount]

def declareWinner(user_1,user_2,user1Amount,user2Amount,data,user_1_bet,user_2_bet):
	temp1 = data[0] % 10
	temp2 = data[1] % 10
	if(temp1 == temp2):
		print("That's tie")
	elif(temp1 > temp2):
		print("Winner is "+str(user_1))	
		finalResult = declareWinnerCalculations1(user_1,user_2,user1Amount,user2Amount,user_1_bet,user_2_bet)
		print(input("\t\t Press enter for an other round...."))
		cardGame(user_1,user_2,finalResult[0],finalResult[1],count = 0,sumOf_1 = 0,sumOf_2 = 0)
	else:
		print("Winner is "+str(user_2))
		finalResult = declareWinnerCalculations2(user_1,user_2,user1Amount,user2Amount,user_1_bet,user_2_bet)
		print(input("\t\t Press enter for an other round...."))
		cardGame(user_1,user_2,finalResult[0],finalResult[1],count = 0,sumOf_1 = 0,sumOf_2 = 0)

def bettingAmount(user_1,user_2,user1Amount,user2Amount,data):
	user_1_bet = int(input(str(user_1)+" enter bet :"))
	user_2_bet = int(input(str(user_2)+" enter bet :"))	
	print("\t\t let's declare winner.....")
	print(input("\t\t Press enter to show off....."))
	declareWinner(user_1,user_2,user1Amount,user2Amount,data,user_1_bet,user_2_bet)		

def cardGameCalculation(sumOf_1,sumOf_2):	
	if(input("are you ready user 1 ?") == 'y'):
		pair = random.choice(list)
		if(type(pair) == int):
			sumOf_1 = sumOf_1 + pair
		else:
			sumOf_1 = sumOf_1 + 10
	else:
		print("user_1 is not ready:")
		
	if(input("are you ready user 2 ?") == 'y'):
		pair = random.choice(list)
		if(type(pair) == int):
			sumOf_2 = sumOf_2 + pair
		else:
			sumOf_2 = sumOf_2 + 10
	else:
		print("user_2 is not ready:")	
	return [sumOf_1,sumOf_2]

def cardGame(user_1,user_2,user1Amount,user2Amount,count,sumOf_1,sumOf_2):
	if((user1Amount > 0) and (user2Amount > 0)):
		while(count < 3):
			data = cardGameCalculation(sumOf_1,sumOf_2)		
			count = count + 1
		print("Cards has been given:")
		bettingAmount(user_1,user_2,user1Amount,user2Amount,data)
	else:
		print("Some of you may have game amount zero")

def initials():
	user_1 = input("Enter your name player1 :") #init[0]
	user_2 = input("Enter your name player2 :") ##init[1]
	user1Amount= int(input("Enter game amount "+str(user_1) + ":")) #init[2]
	user2Amount= int(input("Enter game amount "+str(user_2) + ":")) ##init[3]
	if(user1Amount <= 1000 and user2Amount <= 1000):
		cardGame(user_1,user_2,user1Amount,user2Amount,count,sumOf_1,sumOf_2)
	else:
		print("Main amount not exceed than 1000")	

print("\t\t\t Welcome to the game \t\t\t")
print("\t\t\t Rules of game \t\t\t")
print("\t\t\t User need add main amount \t\t\t")
print("\t\t\t Main amount not more than 1000 \t\t\t")
print("\t\t\t don't bet more than your main amount \t\t\t")
print("\t\t\t good luck!!!! \t\t\t")
print(input("Press enter to start game...."))

initials()


		




		