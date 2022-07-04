"""
Importing array function for declare an array
"""

from array import *

#Decalare an array
my_array = array('i',[500,600,700,800,900])

#Print Array
print(my_array)

#We can also print our array value by calling index number
print(my_array[0])
print(my_array[1])
print()
#We can use for loop to print array index value. It is very time convinent for us
print('Using For Loop')
for i in range(3):
    print(my_array[i])
print()

#If you want to see where your Declared array has been located in memory you can use this function...
print(my_array.buffer_info())

#If you want to add more value in array then you can use append function of array
my_array.append(300)
print(my_array)

#After append you can remove your item from array by using remove function
my_array.remove(300)
print(my_array)

# We can reverse our array
my_array.reverse()
print(my_array)

print()
#We can also check the length of our array using len function
print("Length of Array: ",len(my_array))
