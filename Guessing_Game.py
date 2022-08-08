n =18
i = 0
while i<5:
    print("No Of guesses left: ",5-i)
    x = int(input("Enter Number: "))
    if x<18:
        print("You are So Closer")
        print("Increase Your Value\n")

    elif x>18:
        print("Ohhhh! You Getting up")
        print("Decrease some value\n")

    else:
        print("Congratulations...")
        print("Your Guess is Correct")
        print("Number of Chance Required: ",i+1)
        break

    i = i+1

    if i>5:
        print("Your Chance is Over")
        print("Thank you")
