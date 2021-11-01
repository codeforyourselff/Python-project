#create a program to check a students marks and according to that declare "pass" or "fail"

#take 4 theory subject marks from user
sum1 = 0;
theory_sub = [];
for x in range(0,4,1):
	ele = int(input("Enter theory subject marks:"))
	sum1 = sum1+ele
	theory_sub.append(ele)
print(theory_sub)
print("total in theory marks",sum1)

sum2 = 0;
practicle_sub = [];
for y in range(0,3,1):
	ele = int(input("Enter practicle subject marks:"))
	sum2 = sum2 + ele
	practicle_sub.append(ele)
print(practicle_sub)
print("Total in practicle marks",sum2)

i = 1
count1 = 0
for x in theory_sub:
	if(x >= 50):
		print("Theory",i,"pass")
		i = i +1
	elif(x <= 30):
		count1 = count1+1
		print("")
	else:
		print("Theory","Fail")
print(count1)

j = 1		
count2 = 0
for y in practicle_sub:
	if(y >= 70):
		print("Practicle",j,"Pass")		
		j = j + 1
	elif(y >= 80):
		count2 = count2+1
	else:
		print("Practicle","Fail")
print(count2)

if sum1+sum2 >= 450:
	print("you have cleared examination")



# theory_sub1 = int(input("Enter marks of theroy sub1:"))
# theory_sub2 = int(input("Enter marks of theroy sub2:"))
# theory_sub3 = int(input("Enter marks of theroy sub3:"))
# theory_sub4 = int(input("Enter marks of theroy sub4:"))
# total_of_theory = theory_sub1+theory_sub2+theory_sub3+theory_sub4

# #take 3 practicle subject marks from user
# practicle_sub1 = int(input("Enter marks of practicle sub1:"))
# practicle_sub2 = int(input("Enter marks of practicle sub2:"))
# practicle_sub3 = int(input("Enter marks of practicle sub3:"))
# total_of_practicle = practicle_sub1+practicle_sub2+practicle_sub3

# total_marks = total_of_theory + total_of_practicle

# #now check criteria fro pass or fail according to marks

# if theory_sub >= 50 and theory_sub2 >= 50 and theory_sub3 >= 50 and theory_sub4 >= 50:
# 	print("You have cleared theory exam")
# elif practicle_sub1 >=70 and practicle_sub2 >= 70 and practicle_sub3 >= 70:
# 	print("You have cleared practicle exam")
# elif total_marks >= 450:
# 	print("You have cleared exam")		