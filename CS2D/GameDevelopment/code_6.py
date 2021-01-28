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

img = pygame.image.load('football.png')

x,y = 0,0
move_x, move_y = 2,2
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # screen.fill(white)
    screen.fill(color_1)
    # pygame.draw.circle(screen, color_1, [x, y], 50)
    screen.blit(img, (x,y))
    x += move_x
    y += move_y

    if x >= width - 100:
        move_x = -random.randint(5,20)
    elif x < 0:
        move_x = random.randint(5,20)

    if y >= height - 100:
        move_y = -random.randint(5,20)
    elif y < 0:
        move_y = random.randint(5,20)

    pygame.display.update()


