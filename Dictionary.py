# A dictionary is nothing just key value points
# Lets Know About Python Dictionary

from copy import copy


d1 = {'Shariar':'Burger',
'Jabir':'Pizza',
'Munia':'Chawmin',
'Sijan':'Noodles'}

print(d1)
print(type(d1))

# we can access individual item from a dictionary
print(d1['Jabir'])
print(d1['Shariar'])

#We can also create nested dictionary in Python
d1 = {'Shariar':'Burger',
'Jabir':'Pizza',
'Munia':'Chawmin',
'Sijan':'Noodles',
'Kabir':{'B':'Omlet','L':'Fish','D':'Chicken'}}

print(d1)
print(d1['Kabir'])

#We can also add new value anytime in python dictionary
d1['Rehman'] = 'Parata'
d1['Sajid'] = 'Halim'
d1['Nairobi'] = 'Swarma'
d1[420] = 'Chanachur'

print(d1)

#We can Also delete anytime from dictionary very easily
del d1[420]
print(d1)

# Lets See some function of Dictionary
#copy()
#This function copied item one dictionary to another dictionary
d3 = d1.copy()
print()
print(d3)

#get()
#it will catch the output of required keys
print()
print(d1.get('Shariar'))

#update()
#we can update any value anytime in python
print()
d1.update({'Leena':'Daal'})
print(d1)

#pop()
# We can delete keys and value using pop function
print()
d1.pop('Leena')
print(d1)

#keys()
#this function shows all the keys value inside dictionary
print()
print(d1.keys())

#items()
#this function shows all the item value of dictionary
print()
print(d1.items())
