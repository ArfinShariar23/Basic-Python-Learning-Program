u_input = int(input("Enter any number: "))

if u_input>-1:
    print("This is a Positive Number")
    if u_input%2==0:
        print("This is a Even Number also")
    else:
        print("This is a Odd Number also")

else:
    print("This is a Negative Number")
    if u_input%2 == 0:
        print("This is a Even Number also")
    else:
        print("This is a Odd Number also")

print("Thank you")
