"""A Person Wants to make a Driving License for drive his car. As a Administrator you wants to know the age of person. Now Write a Program to take an 
intiger as his age. If the age is greater then 18 then he will be eligible for driving license.If less then 18 then he will not eligible for driving
license. But If his age equal to 18 then you will send a message to him to meet you physically and after testing you will give his license."""

age = int(input("Please Enter Your Age: "))

if age>18:
	print('You are Eligible for License')

elif age == 18:
	print('We doubt on you. Please Visit BRTA as soon as possible')
	

else:
	print("Sorry! You are not Eligible for License")
	
print('Thank you')