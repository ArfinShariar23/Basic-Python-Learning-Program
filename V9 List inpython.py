
#Creating a List in python

country = ['India','Bangladesh','China','Nepal','Pakistan','Japan','Saudi Arab','Qatar']
print(country) #this will print our country list

#We can Create nested List inside of our list

country = ['India','Bangladesh','China','Nepal',['Bhutan','Sri Lanka','Afganistan'],'Pakistan','Japan','Saudi Arab','Qatar']
print(country) #this will print our Nested List

# We can extend our list by using extend function
country.extend(['Taiwan','Mongolia','Turkey','Nigeria'])
print(country) #this will print country list with extend version

#We can reverse our list using reverse function
country.reverse()
print(country)
print()
#We can iterate item from list by calling their index number
print(country[0])
print(country[-1])
print(country[0:5])
print()

#Using of for loop to iterate item
for i in range(5):
    print(country[i])

#We can append new item or number using append function
country.append('Surinam')
print(country)

#We can remove item from list using remove function
country.remove('Surinam')
print(country)
#Using Pop we can remove last item from very easily:
country.pop()
print(country)

# Count function counts that how many times a specefic value inside the list
x = country.count("Bangladesh")
print(f"We found Bangladesh:{x} times inside the List")

#We can Copy one list to another list

#Creating a null list
#now we copy country list item into friend
friend = country.copy()
print("The New List Friend Print Below")
print(friend)


