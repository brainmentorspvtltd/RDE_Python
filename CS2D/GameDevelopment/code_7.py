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
move_x, move_y = 0,0

enemy_x = random.randint(1,width-50)
enemy_y = random.randint(1,height-50)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 2
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -2
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 2
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -2
                move_x = 0

    screen.fill(white)
    snake_rect = pygame.draw.rect(screen, color_1, [x, y, 50, 50])

    pygame.draw.circle(screen, black, [enemy_x, enemy_y], 20)
    enemy_rect = pygame.Rect(enemy_x,enemy_y,20,20)
    x += move_x
    y += move_y

    if x >= width:
        x = -50
    elif x < -50:
        x = width

    if y >= height:
        y = -50
    elif y < -50:
        y = height

    if enemy_rect.colliderect(snake_rect):
        enemy_x = random.randint(20, width - 50)
        enemy_y = random.randint(20, height - 50)

    pygame.display.update()


