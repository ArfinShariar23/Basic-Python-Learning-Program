#Tuple is a unordered List
#Tuple represent in () brakets

#Creating a tuple

tuple = (1,2,3,4,5,6,7)
print(tuple)

#we can use nested tuple
tuple = (1,2,3,4,(8,9,10),5,6,7)
print(tuple)

#We can iterate item of tuple by calling index number
print(tuple[1])
print(tuple[2])
print(tuple[3])

# we can not insert new item inside tuple like list
# we can not also rplace value in tuple
# we also can not remove single item from tuple
# if we need to delete any item from tuple then we need to clear hole tuple

# tuple take not so much space in memory. It contains less then memory then list
#now we going to check it

import sys
tuple = (1,3,6,7,8)
list = [1,2,3,4]

print("tuple: ",sys.getsizeof(tuple))
print("List: ",sys.getsizeof(list))
