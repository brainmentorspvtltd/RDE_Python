import pygame
pygame.init()

width, height = 1000, 600

screen = pygame.display.set_mode((width, height))
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0

screen.fill(white)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
