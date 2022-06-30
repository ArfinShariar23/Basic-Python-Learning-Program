# Every Data Container in python contain a memory
# Now we discover this one

#Check 1
print('Check 1')
x = 100
print(x)
print(id(x)) # this will print the memory location of x container

#Check 2
print('Check 2')
x = 100
y = 90
print(id(x))
print(id(y))

#Check 3
print('Check 3')
x = 100
y = 90
z = 50+50
print(id(x))
print(id(z)) #This memory location will be similar to memory location of x.
print(id(y))

#Check 4
print('check 4')
x = 100
y = 'Shariar'
z = 10+90

print(id(x))
print(id(z)) #Again Simillar to x.
print(id(y))

"""
Output:
__________

Check 1
100
140706350883584
Check 2
140706350883584
140706350883264
Check 3
140706350883584
140706350883584
140706350883264
check 4
140706350883584
140706350883584
2243877250608

Process finished with exit code 0


"""
