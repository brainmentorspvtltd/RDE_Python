import random

num = random.randint(1,100)

while True:
    guess = int(input("Enter your guess : "))

    if num == guess:
        print("Congrats, You guessed the number")
        break
    elif num > guess:
        print("Number is too short")
    elif num < guess:
        print("Number is too large")
    else:
        print("Invalid input, Please enter a number b/w 1 to 100")
