""" Write a Program which take user input until the input equal or greater then 100. If Input match the condition there will be a message which is 'Congratulation
You Cross the Milestone'"""
while(True):
    inp = int(input("Enter Value: "))
    if inp >=100:
        print("Congratulation You Touched the milestone")
        break

    else:
        print("Try Again")
        continue

    inp = inp+1
