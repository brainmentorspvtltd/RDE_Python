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

screen.fill(white)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # pygame.draw.rect(screen, color_1, [0, 0, 50, 50])
    # pygame.draw.rect(screen, color_1, [100, 100, 50, 50])
    # pygame.draw.rect(screen, color_1, [200, 200, 50, 50])
    for i in range(10):
        for j in range(i + 1):
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pygame.draw.rect(screen, color, [j * 51, i * 51, 50, 50])

    pygame.display.update()


