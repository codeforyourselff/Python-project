#Range data program 
count = 0;
for x in range(1500,2700,1):
	if(x%7 ==0 and x%5 == 0):
		print("Divisible by both:"+str(x))
		count = count +1 
	elif(x%7 == 0):
		print("Divisible by seven:"+str(x))
		count = count + 1
	elif(x%5 == 0):
		print("Divisible by five:"+str(x))
		count = count + 1

print("Total numbers:"+str(count))		

