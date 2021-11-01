#random range programe
#This programe demonstrate the string indexing (positive to negative)

#first we print positive index of program
import random

user_string = input("Enter your string:")

high = len(user_string) 
low = -len(user_string)

for x in range(10):
	position = random.randrange(low,high)
	print([position])