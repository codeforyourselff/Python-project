Number = int(input("Enter a number:"))
zero= 0;
postive = 0;
negetive = 0;

if(Number > 0):
	postive = postive + 1 
elif(Number < 0):
	negetive = negetive + 1
else:
	zero = zero + 1

print("Postitive no is:"+str(postive))
print("Negetive no is:"+str(negetive))
print("Zero no is:"+str(zero))	
