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

def check_winner(pos, ch):
    for i in range(len(winning_combinations)):
        if pos in winning_combinations[i]:
            index = winning_combinations[i].index(pos)
            winning_combinations[i][index] = ch

    for i in range(len(winning_combinations)):
        condition_1 = winning_combinations[i][0] == ch
        condition_2 = winning_combinations[i][1] == ch
        condition_3 = winning_combinations[i][2] == ch
        if condition_1 and condition_2 and condition_3:
            # print("{} Win".format(ch))
            return "win"

    print(winning_combinations)

def user_move(ch):
    pos = int(input("Enter your position : "))
    positions[pos - 1] = ch
    display_gameboard()
    occupied.append(pos)
    msg = check_winner(pos, ch)
    return msg

def cpu_move(ch):
    pos = random.randint(1,9)
    print("CPU Picked",pos)
    if pos in occupied:
        cpu_move(ch)
    else:
        positions[pos - 1] = ch
        display_gameboard()
        occupied.append(pos)
        check_winner(pos, ch)

def game():
    display_gameboard()
    user_ch = input("Enter your choice : 0 | X : ")
    if user_ch == 'X':
        cpu_ch = '0'
    else:
        cpu_ch = 'X'
    while True:
        msg = user_move(user_ch)
        if msg == "win":
            print("User win")
            break

        msg = cpu_move(cpu_ch)
        if msg == "win":
            print("CPU Win")
            break

game()




