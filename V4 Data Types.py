"""
There are 3 data type in Python
1. Numeric
    |_ This is again 4 types:
        1. Intiger
        2. Float
        3. Boolean
        4. Complex
2. Sequence
3. Dictionary
"""

x = 10
y = 10.5
name = 'Shariar'
supershop = ['Apple','Orange','Choclate','Washer']
car = ('Engine','Staring','Break','Hydrolic')
book = {'Life of Pie','Room no 07','365 DAYS','FIFTY SHADES OF GREY'}

print('Checking Intiger')
print("x is a: ",type(x))
print()
print('Checking Float')
print("y is a: ",type(y))
print()
print('Checking String')
print("This name is a: ",type(name))
print()
print('Checking List')
print('The Super Shop is a: ',type(supershop))
print()
print('Checking Tuples')
print('The Car is a: ',type(car))
print()
print('Checking Set')
print('The book are in: ',type(book))
print()
print("Checking Boolean")
if x<y:
    print('True')
    print('This is Condition is: ',type(x<y))
print()

"""
Output:
_________

Checking List
The Super Shop is a:  <class 'list'>

Checking Tuples
The Car is a:  <class 'tuple'>

Checking Set
The book are in:  <class 'set'>

Checking Boolean
True
This is Condition is:  <class 'bool'>


"""

