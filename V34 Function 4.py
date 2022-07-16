#If We add a '*' sign infront agrs then it will take unlimited input as parameter and take them as a tuple item. 
#Then we can easily itterate them using for loop.
#Creating a Function which name is Calculator
def calculator(*args):
	print(type(args))
	temp = 0
	for number in args: #using for loop to iterate our tuple item/value
		temp = temp+number #addition process
	return temp #return our function

temp = calculator(1,2,22,12,17,21,98) #adding value in the temp
print(temp) #printing temp
