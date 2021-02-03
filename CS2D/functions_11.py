def player():
    health = 60
    return health
def enemy():
    health = 67
    return health
def game():
    p_health = player()
    e_health = enemy()
    if p_health > e_health:
        print("Enemy will lose")
    else:
        print("User will lose")
game()