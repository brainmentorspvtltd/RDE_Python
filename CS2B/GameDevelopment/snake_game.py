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

frog = pygame.image.load('frog.png')
frog_w = frog.get_width()
frog_h = frog.get_height()
frog_x = random.randint(0, width - frog_w)
frog_y = random.randint(0, height - frog_h)

snake_w = 50
snake_h = 50

snakeList = []
snakeLength = 1

mixer = pygame.mixer.Sound('point.wav')

x,y = 0,0
move_x, move_y = 0,0

FPS = 100
clock = pygame.time.Clock()

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen, red, [snakeList[i][0],
                                       snakeList[i][1],
                                       snake_w, snake_h])

def score(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render('Score : {}'.format(count), True, black)
    screen.blit(text, (10,10))

count = 0
while True:
    for event in  pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 4
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -4
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 4
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -4
                move_x = 0

    screen.fill(white)
    screen.blit(frog, (frog_x, frog_y))
    snake_rect = pygame.draw.rect(screen, red, [x, y, snake_w,snake_h])
    # snake_rect = pygame.Rect(x, y, snake_w, snake_h)
    frog_rect = pygame.Rect(frog_x, frog_y, frog_w, frog_h)
    x += move_x
    y += move_y

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)
    snakeList.append(snakeHead)

    if len(snakeList) > snakeLength:
        del snakeList[0]

    snake(snakeList)

    if snake_rect.colliderect(frog_rect):
        frog_x = random.randint(0, width - frog_w)
        frog_y = random.randint(0, height - frog_h)
        snakeLength += 10
        FPS += 10
        mixer.play()
        count += 1

    if x > width:
        x = -50
    elif x < -50:
        x = width

    if y > height:
        y = -50
    elif y < -50:
        y = height

    score(count)
    pygame.display.update()
    clock.tick(FPS)
