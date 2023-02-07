# Guess the number game
import random

cpu = random.randint(1,100)
counter = 5

while True:
    user = int(input("Enter your guess : "))

    if cpu == user:
        print("Congrats, You have guessed the number")
        break
    elif cpu < user:
        print("You have guessed a larger number")
    elif cpu > user:
        print("You have guessed a smaller number")
    counter -= 1
    print("Chances Left :",counter)
    if counter == 0:
        print("You lost the game...Number was",cpu)
        break
    







