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

img = pygame.image.load('football.png')

while True:
    for event in  pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    # pygame.draw.circle(screen, color, [x, y], 50)

    screen.blit(img, (x,y))

    x += move_x
    y += move_y

    if x > width - 100:
        move_x = -random.randint(2,10)
    elif x < 0:
        move_x = random.randint(2,10)

    if y > height - 100:
        move_y = -random.randint(2,10)
    elif y < 0:
        move_y = random.randint(2,10)

    pygame.display.update()

