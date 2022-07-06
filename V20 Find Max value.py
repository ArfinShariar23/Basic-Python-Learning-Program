num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))

#For number1 Checking
if num1>num2 and num1>num3:
    print("Number 1 is Max then Number 2 and 3")

#For Number 2 Checking
elif num1<num2 and num2>num3:
    print("Number 2 is greater then Number 1 and 3")

#For Number 3 checking
else:
    print("Number 3 is greater then Number 1 and 2")
