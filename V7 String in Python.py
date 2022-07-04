#Declare a String value
name = 'DATA SCIENCE'

print(name) #it will print variable name

#we can check every letter inside the string by following command
print(name[0:4])

#we can check it from backaward system also
print(name[-7:-4])

address = ' Dhaka Bangladesh '
#we can use strip to remove white space in string

print(address.strip()) # this will remove white space in address

#we can convert any lowercase string in upper case very easy way in python
country = 'bangladesh'

print(country.upper()) #this will convert bangladesh in upper case

#we can also convert any Uppercase value in lower case value in python
country2 = 'INDIA'
print(country2.lower()) #It will convert string value in lower case

#We can also replace value of a string in python very easy way
print(address.replace('Dhaka','Doha')) #It will replace dhaka by Doha
print(address.replace('Bangladesh','Qatar')) #It will replace Bangladesh by Qatar

#We can split our variable in python
print(address.split())
