import random

options = ['stone', 'paper', 'scissor']

cpu_choice = random.choice(options)
user_choice = input("Enter your choice : ")

if cpu_choice == user_choice:
    print("Draw")
elif cpu_choice == 'stone' and user_choice == 'scissor':
    print("CPU Win")
