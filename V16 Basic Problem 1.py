#Find odd even number using conditional statement
user_input = int(input("Enter Any number: "))

if user_input%2 == 0:
    print("Your input is a even number")
elif user_input%2 !=0:
    print("Your input is a odd number")

else:
    print("Input error!!!")
