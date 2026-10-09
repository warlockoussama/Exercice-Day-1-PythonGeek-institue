import random

user_number = int(input("Enter a number from 1 to 9: "))
random_number = random.randint(1, 9)

if user_number == random_number:
    print("Winner")
else:
    print("Better luck next time.")