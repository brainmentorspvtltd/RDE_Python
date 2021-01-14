import random

cpu = random.randint(1,100)
count = 0
while True:
    guess = int(input("Enter the guess : "))
    if cpu == guess:
        print("You guessed the number...")
        break
    elif cpu > guess:
        print("Number is small")
        count += 1
    elif cpu < guess:
        print("Number is greater")
        count += 1

    if count == 5:
        print("You lose")
        break

    print("Count is",count)
