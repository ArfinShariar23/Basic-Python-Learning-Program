def Largest(list):
	max = list[0]
	for x in list:
		if x>max:
			max = x
	
	return x
print(Largest([10,20,30,40,50]))
