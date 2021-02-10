def player_health():
    health = 80
    return health

def enemy_health():
    health = 70
    return health

def game():
    p_health = player_health()
    e_health = enemy_health()
    print("Player Health :",p_health)
    print("Enemy Health :",e_health)
    if p_health > e_health:
        print("User is winning")
    else:
        print("Enemy is winning")

game()