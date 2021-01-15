import random

options = ['stone','paper','scissor']

cpu_score = 0
user_score = 0
while True:
    cpu = random.choice(options)
    user = input("Enter your choice : ")
    print("CPU Picked",cpu)
    if user == cpu:
        print("Draw")
    elif cpu == 'stone' and user == 'scissor':
        print("CPU Win")
        cpu_score += 1
    elif cpu == 'paper' and user == 'stone':
        print("CPU Win")
        cpu_score += 1
    elif cpu == 'scissor' and user == 'paper':
        print("CPU Win")
        cpu_score += 1
    elif cpu == 'stone' and user == 'paper':
        print("You Win")
        user_score += 1
    elif cpu == 'paper' and user == 'scissor':
        print("You Win")
        user_score += 1
    elif cpu == 'scissor' and user == 'stone':
        print("You Win")
        user_score += 1

    print("CPU Score :",cpu_score)
    print("User Score :",user_score)
    
