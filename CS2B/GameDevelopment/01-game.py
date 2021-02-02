import pygame
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
    pygame.display.update()

