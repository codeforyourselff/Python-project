#theory subjects

theory_1 = int(input("Enter theory_1 marks:"))
theory_2 = int(input("Enter theory_2 marks:"))
theory_3 = int(input("Enter theory_3 marks:"))
theory_4 = int(input("Enter theory_4 marks:"))
total_theory = theory_1 + theory_2 + theory_3 + theory_4

#practicle subject

practicle_sub1 = int(input("Enter practicle_1 mark:"))
practicle_sub2 = int(input("Enter practicle_2 mark:"))
practicle_sub3 = int(input("Enter practicle_3 mark:"))
total_practicle = practicle_sub1 + practicle_sub2 + practicle_sub3

total = total_theory + total_practicle
percnt = (total * 100) / 700;
cnt = 0

if (theory_1 >= 50 and theory_2 >= 50 and theory_3 >= 50 and theory_4 >= 50 ) and (practicle_sub1 >= 70 and practicle_sub2 >= 70 and practicle_sub3 >= 70):
	print("Your theory and practicle examination are cleared!")
	if(total >= 450):	
		print("you have sucessfully cleared examination:","Your total is:",total)
	else:
		print("but,your total is not more than 450,failed")

elif(practicle_sub1 >= 80 and practicle_sub2 >= 80 and practicle_sub3 >= 80):
	if(theory_1 >= 25 and theory_1 <= 30):
		cnt = cnt+1 
	if(theory_2 >= 25 and theory_2 <= 30):
		cnt = cnt+1
	if(theory_3 >= 25 and theory_3 <= 30):
		cnt = cnt+1
	if(theory_4 >= 25 and theory_4 <= 30):
		cnt = cnt+1	
	if(cnt == 1):
		if(theory_1 >=25 and theory_1 <= 30):
			print("You will get 5 marks of gracing in","theory_1")
		elif(theory_2 >=25 and theory_2 <= 30):
			print("You will get 5 marks of gracing in","theory_2")
		elif(theory_3 >=25 and theory_3 <= 30):
			print("You will get 5 marks of gracing in","theory_3")
		else:
			print("You will get 5 marks of gracing in","theory_4")
	if(cnt > 1):
		print("You are not eligible for gracing,you failed in more than 1 theroy sub")	
else:
	print("you have not cleared theory or practicle examination")				
#Grading system

if(percnt >= 90 and percnt < 100):
	print("Grade-A")
elif(percnt >= 70 and percnt < 90):
	print("Grade-B")	
elif(percnt >= 50 and percnt < 70):
	print("Grade-C")
elif(percnt >= 35 and percnt < 50):
	print("Grade -D")


		

