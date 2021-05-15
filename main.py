import sys, pygame
pygame.init()

pygame.display.set_caption('test caption')

size = width, height = 320, 240
ball_speed = 2
speed = [ball_speed, ball_speed]
ball_speed_curr = speed
black = 200, 0, 0
ballSize= 10
screen = pygame.display.set_mode(size)
GameSpeed=20
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
space_pressed = False
ball_moving = True

while 1:
    GameClock=pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN and pygame.K_SPACE and space_pressed == False:
            space_pressed = True
        if space_pressed and event.type == pygame.KEYUP:
            space_pressed = False

    if space_pressed:
        if ball_moving:
            ball_speed_curr = speed[:]
            speed[0] = 0
            speed[1] = 0
            ball_moving = False
        else:
            speed = ball_speed_curr[:]
            ball_moving = True
        space_pressed = False

    GameClock.tick(GameSpeed)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
pygame.quit()
