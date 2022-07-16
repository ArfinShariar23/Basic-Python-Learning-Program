#Print the Multiplication table of user input. Take an user input from user which is a int value
input1 = int(input("Enter any number: "))
count = 1

for x in range (1,11):
	print(input1,"x",count,"=",input1*count)
	count = count+1
print("Finished")