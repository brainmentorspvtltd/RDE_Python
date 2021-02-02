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
    pygame.draw.rect(screen, red, [x, y, 50,50])
    x += move_x
    y += move_y

    if x > width - 50:
        move_x = -2
    elif x < 0:
        move_x = 2

    if y > height - 50:
        move_y = -2
    elif y < 0:
        move_y = 2

    pygame.display.update()

