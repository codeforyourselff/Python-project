import random #random module to use randomize number between range

#This is a guessing number program
#This program contain functions

random_num=random.randint(1,6)

print("\n \"Welcome to guessing number machine!\" \n")
print("Rules:")
print("\t--You have to guess the number between 1-6,")
print("\t--you got limited trials,")
print("\t--be the game changer.\n")

trials=3
while trials<4 and trials>0:
	user_num=int(input("Okay!lets guess the number-->>"))

	if user_num!="":
		if user_num==random_num:
			print("Congratulations!You have done it!")
			trials-=1
			print("you have remaining trials",trials,"but you have done it")
			print("--------------------------------")
			break
		elif user_num!=random_num:
			print("Nope!thats not the correct number")
			trials-=1
			print("try harder! remaining trials",trials)
			print("--------------------------------")
			continue	
		else:
			print("can't understand your input \n")	
	else:
		print("Please input number!")		

if(trials==0 and user_num!=random_num):
	print("Ohh!better luck next time \n")

input("Thank you for playing!Press any key to exit.... \n")