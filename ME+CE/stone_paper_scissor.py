import random

options = ['stone', 'paper', 'scissor']
chances = 1
user_score = 0
cpu_score = 0
while chances < 11:
    print("Chance :",chances)
    cpu_choice = random.choice(options)
    user_choice = input("Enter your choice : ")
    print("CPU Picked :",cpu_choice)

    if cpu_choice == user_choice:
        print("Draw")
    elif cpu_choice == 'stone' and user_choice == 'scissor':
        print("CPU Win")
        cpu_score += 1
    elif cpu_choice == 'paper' and user_choice == 'stone':
        print("CPU Win")
        cpu_score += 1
    elif cpu_choice == 'scissor' and user_choice == 'paper':
        print("CPU Win")
        cpu_score += 1
    elif cpu_choice == 'stone' and user_choice == 'paper':
        print("User Win")
        user_score += 1
    elif cpu_choice == 'paper' and user_choice == 'scissor':
        print("User Win")
        user_score += 1
    elif cpu_choice == 'scissor' and user_choice == 'stone':
        print("User Win")
        user_score += 1

    chances += 1

print('*' * 40)

print("Final Score : ")
print("CPU : {}, User : {}".format(cpu_score, user_score))
if cpu_score == user_score:
    print("Match Draw")
elif cpu_score > user_score:
    print("CPU Wins")
else:
    print("User Wins")








