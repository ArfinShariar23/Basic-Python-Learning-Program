#Python Sets
#Python Sets is like List and tuple
#But It cannot take any duplicate value like List and tuple

#Let's Create a sets...
set1 = {1,2,3,4,5,6}
set3 = {2,3,4,6,9,1}
set4 = {9,10,6,7,5,3,2}
print(set1)

#We can create set by using list format with set function
list = set([1,2,3,4,5,6]) #This is a set but it will print output in set format
print(list)

#Let's use of funcition for set
#we can add new value or item in set
set1.add(7)
print(set1)

#We can Remove item from set using remove function
set1.remove(7)
print(set1)

#we can also pop item from set.It will remove first item from set
set1.pop()
print(set1)

#We can discard hole set
set1.discard(4)
print(set1)

#We can copy item in set
set2 = set1.copy()
print(set2)

#We can check Union of 2 set
if set1.union(set2):
    print("They are union")
else:
    print("They are not")

#We can check intersect of 2 sets
x = set1.intersection(set3)
y = set1.intersection(set4)
z = set1.intersection(set3,set4)
print("After Intersection of set1 and set3 Value remain: ",x)
print("After Intersection of Set1 and Set4 value remain: ",y)
print("After Intersection of Set1 with Set3 and Set4 value remain: ",z)

# We can also check symetric difference of Two Sets
a = set1.symmetric_difference(set3)
print("Symmetric Difference Found: ",a)

#We can also check difference of Two sets
b = set1.difference(set3)
print('Difference of Set1 and Set3 is = ',b)
# We can also convert a list into set again a set into list by removing Duplicate value
#Create a set

count = ['Bangladesh','Japan','Bangladesh','China','India','Pakistan','Bangladesh']
result = set(count)
print(result)

