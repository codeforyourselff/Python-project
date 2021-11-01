# #Finding prime number using function
# def findPrimeNumber(start,end):
# 	flag = False 
# 	for x in range(start,end+1):
# 		for y in range(2,(x//2) +1):
# 			if(x%y == 0):
# 				break
# 			else:
# 				flag = True
# 		if(flag == True):
# 			print(x)
# 			flag = False
# findPrimeNumber(int(input("Enter start point:")),int(input("Enter end point:")))	
# 	

def primeNumber(start,end):
    for x in range(start,end+1):
      for y in range(2,(x//2) +1):
        if(x%y == 0):
          break
        else:
          return x,primeNumber(x+1,end)
print(primeNumber(int(input("Enter start range:")),int(input("Enter end range:"))))

	


