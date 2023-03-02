def sum(num1,num2):
    result = num1+num2
    print("Sum is = ",result)

def sub(num1,num2):
    substraction = num1-num2
    print("Substraction = ",substraction)

def mul(num1,num2):
    mult = num1*num2
    print("Multiplication = ",mult)

def div(num1,num2):
    division = num1/num2
    print("Division is = ",division)

def mod(num1,num2):
    modulas = num1%num2
    print("Modulas = ",modulas)

def exit_func():
    print("Thanks for Using our Calculator")
    print("You are welcome always")
    print("Developed By Arfin Shariar")

print("Welcome to Basic Calculator")
print("---------------------------")
print("For Sum press = 1")
print("For Sub press = 2")
print("For mult press = 3")
print("For div press = 4")
print("For Mod press = 5")
choice = int(input("Enter Your Selection: "))
print()
print()
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print()
print()
if choice == 1:
    sum(num1,num2)
elif choice == 2:
    sub(num1,num2)
elif choice == 3:
    mul(num1,num2)
elif choice==4:
    div(num1,num2)
elif choice == 5:
    mod(num1,num2)
else:
    exit()
print()
print()
exit_func()
