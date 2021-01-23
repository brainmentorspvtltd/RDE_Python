import pygame
pygame.init()

width, height = 1000, 600

screen = pygame.display.set_mode((width, height))
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0

x = 0
y = 0

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.rect(screen,red,[x,y,50,50])
    #pygame.draw.rect(screen,red,[100,100,50,50])
    x += 1
    pygame.display.update()





