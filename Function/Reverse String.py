def reverse_string(sentence):
    print("The Reverse of the Following String = ",sentence[::-1])

number = int(input("Define How Many String do you want to Reverse = "))
for i in range(1,number+1):
    sentence = input("Enter Your String Value Here: ")
    reverse_string(sentence)
