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

screen.fill(white)

while True:
    for event in  pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # pygame.draw.rect(screen, red, [0, 0, 50,50])
    # pygame.draw.rect(screen, red, [100, 100, 50, 50])
    # pygame.draw.rect(screen, red, [200, 200, 50, 50])

    # for i in range(15):
    #     pygame.draw.rect(screen, red, [i * 51, 0, 50, 50])

    for i in range(10):
        for j in range(i + 1):
            color = random.randint(0,255), random.randint(0,255), random.randint(0,255)
            pygame.draw.rect(screen, color, [51 * j, 51 * i, 50, 50])

    pygame.display.update()

