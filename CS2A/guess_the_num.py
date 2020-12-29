import random

num = random.randint(1,100)

COUNT = 0
game = True
while game:
    guess = int(input("Enter your guess : "))
    if guess == num:
        print("Congrats, You guessed the number right")
        game = False
    elif guess > num:
        print("You guessed a larger number")
    elif guess < num:
        print("You guessed a smaller number")
    COUNT += 1
    if COUNT == 5:
        game = False

if not game:
    print("You lose, Number was",num)
    
