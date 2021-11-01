# #Return amount
def case1():
	mainAmount = int(input("Enter an amount to borrow:"))
	no = mainAmount
	i = 0
	dayCount = 1
	if(input("pay day by day ?:") == "y"):
		while(True):
				if((2 ** i) < mainAmount):
					mainAmount = mainAmount - (2 ** i)
					print("At day"+str(dayCount) + ":" + str(2 ** i))
					i = i + 1
					dayCount = dayCount + 1		
				else:
					dayCount = dayCount +1 
					print("At day"+str(dayCount)+ ":" + str(mainAmount))
					print("interest:"+str((no * 10) // 100)+" rs")
					break
	else:
		print("interest:"+str((no * 8) // 100)+"rs")
###interest calculate day by day:		
def case2():
	mainAmount = int(input("Enter an amount:"))
	finalAmount = mainAmount
	rupess = 2 
	i = 0
	day = 1
	if(input("Wnat to pay day by day?:") == "y"):
		while(mainAmount > 0):
			interest = (mainAmount * 10) / 100
			amtWithInterest = mainAmount + interest
			if((rupess ** i) > amtWithInterest):
				print("At day: "+str(day)+" this much amount left:"+str(finalAmount - mainAmount))
				break
			else:
				mainAmount = amtWithInterest - (rupess ** i)
				print("At day: "+str(day)+" this much amount left:"+str(mainAmount))
				i = i + 1
				day = day + 1 
		else:
			print("Please provide greater than 0 value")		
	else:
		print("please put 'y' input")



def intestCalculate(x):
	switcher = {

		1 : case1(),
		2 : case2()
	}

print("\t Enter your choice to calculate days and interest \t")
print("\t Press 1 for calculate \t")
print("\t Press 2 for calculate day by day interest")
print("\n")

intestCalculate(int(input("Enter your choice:")))	





