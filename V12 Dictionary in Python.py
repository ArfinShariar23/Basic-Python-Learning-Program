# A dictionary is a Collection which is unordered with index number.
#It can contain same value
#It represent with {} brackets
#Lets Create a Dictionary

dic1 = {'Name':'Arfin','Age':23,'City':'Dhaka'}
dic2 = {'Name':'Shariar','Age':24,'City':'Frankfruit'}
dic3 = {'Name':'Arif',10:10,10.5:10.5,(10,23,45):'Abir'}
print(dic1)
print(dic2)
print(dic3)

#We can check key name in dictionary
print(dic1.keys())
print(dic3.keys())

#we can copy value in dictionary
dic4 = dic3.copy()
print(dic4)

#We can count values
x = len(dic1)
print('Items found: ',x)

#We can add new item in dictionary
dic1['Versity'] = 'North South University'
print('After adding versity in dic1: ',dic1)

#we can delete item using pop function
dic1.pop('Versity')
print(dic1)

#We can clear our hole dictionary using clear function
dic1.clear()
print("dic1 after clearing: ",dic1)

#We can also delete a dictionary
"""del dic1
print(dic1)"""
