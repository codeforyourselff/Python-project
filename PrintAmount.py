#Seperate decimal and fractional number
number = input("Enter number:")
result = number.split(".")

print("Rupees is:",result[0],"and paisa is:",result[1])