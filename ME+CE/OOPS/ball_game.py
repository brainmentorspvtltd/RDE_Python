import random
import pygame
pygame.init()

class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        self.move_x = random.randint(1,10)
        self.move_y = random.randint(1,10)

    def update(self):
        self.x += self.move_x
        self.y += self.move_y

        if self.x > width - 50:
            self.move_x = -random.randint(1,10)
        elif self.x < 50:
            self.move_x = random.randint(1,10)

        if self.y > height - 50:
            self.move_y = -random.randint(1,10)
        elif self.y < 50:
            self.move_y = random.randint(1,10)

width = 1200
height = 600
resolution = width, height
screen = pygame.display.set_mode(resolution)
white = 255,255,255

# ball_1 = Ball()
# ball_2 = Ball()
# ball_3 = Ball()

balls = []
for i in range(100):
    ball = Ball()
    balls.append(ball)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    # pygame.draw.circle(screen, ball_1.color, [ball_1.x, ball_1.y], 50)
    # ball_1.update()
    #
    # pygame.draw.circle(screen, ball_2.color, [ball_2.x, ball_2.y], 50)
    # ball_2.update()
    #
    # pygame.draw.circle(screen, ball_3.color, [ball_3.x, ball_3.y], 50)
    # ball_3.update()

    for i in range(len(balls)):
        pygame.draw.circle(screen, balls[i].color, [balls[i].x, balls[i].y], 50)
        balls[i].update()


    pygame.display.update()