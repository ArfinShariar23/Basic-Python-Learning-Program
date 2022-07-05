# today we will learn nested dictionary

student = {1:{"Name":"Arif","Age":21,"Address":"Dhaka"},
           2:{"Name":"Shuvo","Age":20,"Address":"Khulna"},
           3:{"Name":"Polash","Age":21,"Address":"Noakhali"}
           }

print(student)
print()
#we access item from nested dictionary by calling their keys
print(student[1]['Name'])
print(student[2]["Age"])
print(student[3]["Address"])
print()

#we can also add new item in nested dictionary
student[4] = {}
student[4]["Name"] = 'Shakib'
student[4]['Age'] = 23
student[4]['Address'] = 'Faridpur'

print(student[4])
print()
#use del keyword to delete hole dictionary
del student[4]['Address']
print("After Deleting Address from student 4")
print(student[4])
