def playerHealth():
    health = 80
    return health

def enemyHealth():
    health = 75
    return health

def game():
    p_health = playerHealth()
    e_health = enemyHealth()
    print("Player Health :",p_health)
    print("Enemy Health :",e_health)

game()