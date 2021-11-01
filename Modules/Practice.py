#dictonary
lst = []

dis1 = {"Name":"Krishna","age":25,"Location":"Ahmedabad"}
dis2 = {"Name":"Jaimin","age":22,"Location":"Ahmedabad"}
dis3 = {"Name":"Jilani","age":21,"Location":"Ahmedabad"}

lst.append(dis1)
lst.append(dis2)
lst.append(dis3)
for x in range(len(lst)):
	print(lst[x]["Location"])


