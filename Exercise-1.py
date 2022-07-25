# Create a Dictionary and take input from user and return the meaning of the word from the dictionary
# Let's Do it....

#Creating a Dictionary
my_dic = {'Shariar':{'Name':'Arfin Shariar','DOB':'23rd July,2000','Age':'22','Emp ID':'DZ0001'},
'Junaid':{'Name':'Junaid Ahmed','DOB':'11th November,1999','Age':'23','Emp ID':'DZ0002'},
'Parsha':{'Name':'Parsha Evana','DOB':'03rd June,2001','Age':'21','Emp ID':'DZ0003'},
'Sabbir':{'Name':'Sabbir Ahmed','DOB':'28th Februrary,2000','Age':'22','Emp ID':'DZ0004'},
'Shakib':{'Name':'Shakib Al Hasan','DOB':'05th September,2000','Age':'22','Emp ID':'DZ00005'}}

print("Welcome to S3Solution")
search = input("Enter Employee Name:")

print(my_dic[search])
print("Thank you for using our System")

