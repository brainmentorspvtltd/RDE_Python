import pygame, random
pygame.init()

# 1. build screen
width = 1200
height = 600
resolution = width, height
screen = pygame.display.set_mode(resolution)

# rgb - red, green, blue
white = 255,255,255
black = 0,0,0
red = 255,0,0
color =  120,100,210

x,y = 0,0
move_x, move_y = 2,2
while True:
    for event in  pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    pygame.draw.circle(screen, color, [x, y], 50)
    x += move_x
    y += move_y

    if x > width - 50:
        move_x = -2
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    elif x < 50:
        move_x = 2
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    if y > height - 50:
        move_y = -2
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    elif y < 50:
        move_y = 2
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    pygame.display.update()

