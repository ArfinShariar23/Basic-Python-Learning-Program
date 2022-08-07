u_input = input("Enter Anything: ")
if u_input[0] == '#' and u_input[1] == '#':
    print("This is a Single Line Comment")

elif u_input[0] == '*' and u_input[1] == '*' and u_input[2] == '*':
    print("This is a Multiple Line Comment")

else:
    print("This is not a Comment")

