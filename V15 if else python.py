#Basic If-else program

x = 100
y = 50
z = 150

if x>y: #this condition will check that is our x is greater then y or y os greater then x
    print("X is big") #if x greater then y happen then this code will be exicute
else:
    print("Y is big") # if y greater then x happen then this code will be exicute

print("Thanks for checking")


#Again use of and,or

if x>y and x>z:
    print("x is greater then all")
elif y>x and y>z:
    print("y is greater then all")
else:
    print("z is greater then all") #this will be exicute

print("Thank you again for checking")
