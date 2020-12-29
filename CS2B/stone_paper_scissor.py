import random

choices = ['stone', 'paper', 'scissor']
user_score = 0
cpu_score = 0
while True:
    cpu_ch = random.choice(choices)
    user_ch = input("Enter your choice : ")
    print("CPU Picked",cpu_ch)
    if user_ch == cpu_ch:
        print("Match Tie")
    elif user_ch == 'stone' and cpu_ch == 'paper':
        print("CPU Win")
        cpu_score += 1
    elif user_ch == 'paper' and cpu_ch == 'scissor':
        print("CPU Win")
        cpu_score += 1
    elif user_ch == 'scissor' and cpu_ch == 'stone':
        print("CPU Win")
        cpu_score += 1
    elif user_ch == 'stone' and cpu_ch == 'scissor':
        print("User Win")
        user_score += 1
    elif user_ch == 'paper' and cpu_ch == 'stone':
        print("User Win")
        user_score += 1
    elif user_ch == 'scissor' and cpu_ch == 'paper':
        print("User Win")
        user_score += 1

    print("CPU : {}, User : {}".format(cpu_score, user_score))    
    if user_score == 5 or cpu_score == 5:
        break

print("Final : CPU : {}, User : {}".format(cpu_score, user_score))
