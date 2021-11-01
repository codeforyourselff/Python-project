first_name=input("Enter first name:")
last_name=input("Enter last name:")
j=0
k=0
for fn in first_name:
    j+=1
for ln in last_name:
    k+=1


print("count of first_name",j)
print("count of last_name",k)
j-=1
k-=1

while(j>=0):
    print(first_name[j])
    j-=1
print("\n")
while(k>=0):
    print(last_name[k])
    k-=1



