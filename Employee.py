#create program to calculate gross salary of an employee

#ask first users basic salary
basic_salary = int(input("Enter your basic salary:"))
total_salary = 0;

if(basic_salary >= 25000):
	da = (basic_salary * 10) / 100
	hra = (basic_salary * 5) / 100
	ta = (basic_salary * 2) / 100
	total_salary = basic_salary+ta+da+hra
	print("Your total salary would be:",total_salary)

elif basic_salary > 15000 and basic_salary < 25000:
	da = (basic_salary * 15) / 100
	hra = (basic_salary * 10) / 100
	ta = (basic_salary * 5) / 100
	total_salary = basic_salary+ta+da+hra
	print("Your total salary would be:",total_salary)

elif basic_salary <= 15000:
	da = (basic_salary * 20) / 100
	hra = (basic_salary * 15) / 100
	ta = (basic_salary * 7) / 100
	total_salary = basic_salary+ta+da+hra
	print("Your total salary would be:",total_salary)
	