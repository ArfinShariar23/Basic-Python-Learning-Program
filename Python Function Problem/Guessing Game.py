def start():
    print("Welcome to Guess Game World")
    print("---------------------------")
def winner_greet():
    print("Congratulations!")
    print("You Guess the Correct Number")
guess_value = [10,12,14,15,18]
start()
print()
print()
print("For Start Press - s")
print("For Exit Press - e")
choice = input("Enter Your Choice: ")
if choice == 's' or choice == 'S':
    guess = int(input("How Many Guess Chance Do you Want = "))
    count = guess
    for i in range(1,guess+1):
        guess_number = int(input("Enter Your Guess Value: "))
        if guess_number in guess_value:
            winner_greet()
            break
        elif guess_number not in guess_value:
            print("Sorry! Go for Next Chance!")
            count -= 1
            if count == 0:
                print("Sorry You Have No More Chance Left!")
                break
            else:
                continue

        else:
            pass
else:
    exit()

