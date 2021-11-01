#Create a rpogram of cricket where two players randomly play
#import random number generator using random package
import random

#take a user input of name
wickets = [0,1,2,3,4,5,6,"bowled","run-out","catch","lbw"];
user_name1 = input("Enter player 1 name:")
user_name2 = input("Enter player 2 name:")
over = int(input("Overs?:"))
user1_wickets = int(input("Enter wickets:"))
user2_wickets = int(input("Enter wickets:"))
count = 0;
player1_total = 0;
player2_total = 0;
if(over == 2 or over == 5):
	if(over == 2):
			while count < 12:
				if(user1_wickets != 0):	
					if(input("Player1 is ready:") == "y"):
						player1_score = random.choice(wickets)
						print(player1_score);
						if(type(player1_score) == int):
							player1_total = player1_total+player1_score
							count = count+1	
						else:
							user1_wickets = user1_wickets - 1;
							count = count+1
				else:
					print("You are out of wickets:"+user_name1)
					break

				if(user2_wickets != 0):				
					if(input("Player2 is ready:") == "y"):
						player2_score = random.choice(wickets)
						print(player2_score)
						if(type(player2_score) == int):
							player2_total = player2_total+player2_score
							count = count+1
						else:
							count = count+1
				else:
					print("You are out of wickets:"+user_name2)
					break
								
	if(over == 5):
			while count < 30:
				if(user1_wickets != 0):	
					if(input("Player1 is ready:") == "y"):
						player1_score = random.choice(wickets)
						print(player1_score)
						if(type(player1_score) == int):
							player1_total = player1_total+player1_score
							count = count+1
						else:
							user1_wickets = user1_wickets - 1;
							count = count+1	
				else:
					print("You are out of wickets:"+user_name1)
					break

				if(user2_wickets != 0):				
					if(input("Player2 is ready:") == "y"):
						player2_score = random.choice(wickets)
						print(player2_score)
						if(type(player2_score) == int):
							player2_total = player2_total+player2_score
							count = count+1
						else:
							count = count+1
					else:
						print("User is not ready")					
						count = count+1
				else:
					print("You are out of wickets:"+user_name2)
					break		

if(player1_total > player2_total):
	print(user_name1,"wins",player1_total)
else:
	print(user_name2,"wins",player2_total)

print("Player1",user_name1,"score is :",player1_total)
print("Player2",user_name2,"score is :",player2_total)	


input("Press enter to exit..................")


