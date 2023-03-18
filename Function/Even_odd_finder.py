#Creating Function
def even_odd_differntiator(number):
    even_numbers = []
    odd_numbers = []
    for num in number:
        if num%2==0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    print("New List of Even Numbers: ",even_numbers)
    print("New List of Odd Numbers: ",odd_numbers)

# Input
random_number = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16]

#Calling Function
even_odd_differntiator(random_number)
