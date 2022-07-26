# We can also give condition in List to find desire item 

List1 = ['Shariar','Arfin','Abir','Apurbo','Nisham','Junaid']
search = input("Entere Name: ")
if search in List1:
	print("Item Found!")
elif search not in List1:
	print("Item Not Found!")
else:
	print('Invalid Input')