import pygame
import random
pygame.init()

width = 1200
height = 600
resolution = width, height
screen = pygame.display.set_mode(resolution)

white = 255,255,255
black = 0,0,0
color_1 = 200,100,155

x,y = 0,0
move_x, move_y = 2,2
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    pygame.draw.circle(screen, color_1, [x, y], 50)
    x += move_x
    y += move_y

    if x >= width - 50:
        move_x = -2
    elif x < 50:
        move_x = 2

    if y >= height - 50:
        move_y = -1
    elif y < 50:
        move_y = 1

    pygame.display.update()


