import random

cpu = random.randint(1,100)
chance = 0
while True:
    num = int(input("Enter your guess : "))

    if cpu == num:
        print("Congrats, You guessed the number...")
        break
    elif cpu > num:
        print("You guessed a smaller number")
        chance += 1
    elif cpu < num:
        print("You guessed a large number")
        chance += 1
    print("Chance : ",chance)

    if chance == 5:
        print("You lose...Number was :",cpu)
        break
