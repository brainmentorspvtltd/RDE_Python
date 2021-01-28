import pygame
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

    pygame.display.update()


