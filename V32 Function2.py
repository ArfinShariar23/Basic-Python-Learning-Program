# Using a Function make a Simple Calculator which will do addition of Three Number....

#creating a Function
def calculator(a,b,c):
	sum = a+b+c
	print("Sum of Three number is: ",sum)
	return

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

calculator(num1,num2,num3)

print("Thank you")