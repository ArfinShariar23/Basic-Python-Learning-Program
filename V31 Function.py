#Creating a Function...
def myname(name):
	print("My Name is: ",name)
	return

#Creating another function...
def myage(age):
	print("Your Age is: ",age)
	return

#Creating one function...
def mygender(gender):
	print("Gender: ",gender)
	return 

#taking user input
input1 = input("Enter Your Name: ")
input2 = int(input("Enter Your Age: "))
input3 = input("Enter Your Gender: ")

#Calling Function
myname(input1)
myage(input2)
mygender(input3)