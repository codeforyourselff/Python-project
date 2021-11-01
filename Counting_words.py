#Counting_words_program

#This program is created through "for loop"
#First take a string from user and print it

user_name = input("Enter your name:")
count=0
print("message length:",len(user_name))
if "a" in user_name:
	print("a comes in your letters")
for x in user_name:
	print(x,end="\n")
	count+=1

print("Total count of string",count)	