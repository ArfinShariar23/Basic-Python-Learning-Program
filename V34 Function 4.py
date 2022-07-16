
def calculator(*args):
	print(type(args))
	temp = 0
	for number in args:
		temp = temp+number 
	return temp 

temp = calculator(1,2,22,12,17,21,98)
print(temp)