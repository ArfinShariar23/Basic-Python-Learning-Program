# Creating Function
def string_len(strings):
    length = 0
    for string in strings:
        length += len(string)
    print("Length of String = ",length)
    
# Input Container
string = ["Arfin","Shariar","Apurbo"]
sentence = "A Quick Brown Fox Jump overhead the wall"

# Calling Function
string_len(string)
string_len(sentence)
