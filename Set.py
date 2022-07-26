#Python Sets is a collection
s = {1,2,3,4}
print(s)
print(type(s))

#we can input value of a set using list type
#Let's Do it
s1 = [1,2,3,4,5,6]
s_from_list = set(s1)
print(s_from_list)
print(type(s))

#We can also do this same thing inside the set
s_from_list1 = set([1,2,3,4,5,6,7,8])
print(s_from_list1)
print(type(s_from_list1))
print()
#we can add item in set anytime
s.add(5)
s.add(6)
s.add(7)
print("After Adding new item in the s: ",s)

#Let's see some module of set
#union()
print(s.union(s_from_list1))

#intersection
print(s.intersection(s_from_list1))

#Check len
print("The Length of s set is:",len(s))

#min
print("The minimum value in s set:",min(s))

#max
print('The Max of s set is:',max(s))

#difference
print("The Difference between S and S_from_list1: ",s.difference(s_from_list1))
