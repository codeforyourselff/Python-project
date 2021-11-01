#Guessing_number game
print("\t Welcome to guessing number game \t")
print("\t you have to guess a number between 1 to 10 \t")
print("\t And you will get only 5 chances \t")

count = 1
ans = 7
number = int(input("Enter a number:"))

while number in range(1,11):
	if (count > 0):
		if(number == ans):
			print("Congretulations!you wins")
			count = count - 1
			break;
		elif(number > ans):
			print("Little large no,try for smaller")
			count = count - 1
			number = int(input("Enter a number:"))
		elif(number < ans):
			print("Liitle smaller no,try for larger")	
			count = count - 1
			number = int(input("Enter a number:"))
	else:
		print("Your have left"+str(count)+"count")
		break		
else:
	print("Number is not in range:")
print("left count:"+str(count))			

# while(True):
# 	if count > 0:
# 		guessing_number = int(input("Enter a guessing number:"))
# 		if(guessing_number >=1 and guessing_number <=10):	
# 			if(guessing_number == number):
# 				print("Congretulations!you wins")
# 				count = count - 1
# 				print("left count:"+str(count))
# 				break
# 			elif(guessing_number > number):
# 				print("to larger number!try for smaller")	
# 				count = count - 1
# 				print("left count:"+str(count))
# 			elif(guessing_number < number):
# 				print("to small number!try for larger")
# 				count = count - 1
# 				print("left count:"+str(count))
# 			elif(guessing_number == type('str')):
# 				print("String not allowed")
# 				count = count - 1
# 				print("left count:"+str(count))
# 			else:
# 				print("Not understand your input")
# 				count = count - 1
# 				print("left count:"+str(count))
# 		else:
# 			print("Please enter between 1 to 10 range")
# 			break
# 	else:
# 		print("You have completed your count you loose :/")							
# 		break

# print(input("Press any key to exit ........."))		

# inputNumber = int(input("Enter a number:"))

# while inputNumber not in range(10):
# 	inputNumber = int(input("Enter a number:"))
# else:
# 	print("correct:")	

