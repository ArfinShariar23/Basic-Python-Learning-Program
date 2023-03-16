#Function for Addition
def sum(num1,num2):
    sum = num1+num2
    print("Sum = ",sum)
#Function for Substraction
def sub(num1,num2):
    if num1>num2: 
        sub = num1-num2
        print("Sub = ",sub)
    else:
        sub = num2-num1
        print("Sub = ",sub)
#Function for Multiplication
def mul(num1,num2):
    mul = num1*num2
    print("Mul = ",mul)
#Function for Division
def div(num1,num2):
    if num1>num2:
        div = num1/num2
        print("Div = ",div)
    else:
        div = num2/num1
        print("Div = ",div)
#Main Driver Code
#Choose option for User
print("For Sum press = 1")
print("For Sub press = 2")
print("For Mul press = 3")
print("For Div press = 4")
print("For Exit press any keys except this 4 keys")
choose = int(input("Enter Your Choice: ")) #Taking User Choose value
print()
print()
#User Value Input
num1 = int(input("Enter First Number: ")) #For Number 1
num2 = int(input("Enter Second Number: ")) #For Number 2

#Calling Function
if choose==1:
    sum(num1,num2) #Sum Function
elif choose==2:
    sub(num1,num2) #Substraction Function Call
elif choose==3:
    mul(num1,num2) #Multiplication Function Call
elif choose==4:
    div(num1,num2) #Division Function Call
else:
    exit()


