import random

winning_combinations = [[1,2,3],[4,5,6],[7,8,9],
                        [1,4,7],[2,5,8],[3,6,9],
                        [1,5,9],[3,5,7]]

positions = [1,2,3,4,5,6,7,8,9]
occupied = []
def display_gameboard():
    print("""
    {} | {} | {}
    -----------
    {} | {} | {}
    -----------
    {} | {} | {}
    """.format(positions[0], positions[1], positions[2],
               positions[3], positions[4], positions[5],
               positions[6], positions[7], positions[8]))

def check_winner():
    pass

def user_move(ch):
    pos = int(input("Enter your position : "))
    positions[pos - 1] = ch
    display_gameboard()
    occupied.append(pos)

def cpu_move(ch):
    pos = random.randint(1,9)
    print("CPU Picked",pos)
    if pos in occupied:
        cpu_move(ch)
    else:
        positions[pos - 1] = ch
        display_gameboard()
        occupied.append(pos)

def game():
    display_gameboard()
    user_ch = input("Enter your choice : 0 | X : ")
    if user_ch == 'X':
        cpu_ch = '0'
    else:
        cpu_ch = 'X'
    while True:
        user_move(user_ch)
        cpu_move(cpu_ch)

game()




