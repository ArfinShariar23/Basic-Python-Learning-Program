#Find the number which are divided by 3 but not divided by 5. Range 1-100
list1 = []
for i in range(1,101):
	if i%3==0 and i%5!=0:
		list1.append(i)

print(list1)

list2 = []
for i in range (1,201):
	if i%5==0 and i%7!=0:
		list2.append(i)

print(list2)

