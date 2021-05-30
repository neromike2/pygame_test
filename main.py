import sys, pygame
import random
pygame.init()

def resetBall():
    ballrect.left = width / 2
    ballrect.top = height / 2
    if random.randint(0,1):
        speed[0] *= -1
    if random.randint(0, 1):
        speed[1] *= -1

def overlap(lower1, upper1, lower2, upper2):
    return(not(lower1 > upper2 and lower2 > upper1))

paddleSpeed = 12
pygame.display.set_caption('test caption')
size = width, height = 940, 480
speed = [10, 10]
ball_speed_curr = speed
backgroundColor = 200, 200, 200
paddleColor = 0, 0, 0
textColor = 50, 50, 50
ballSize = 30
screen = pygame.display.set_mode(size)
GameSpeed = 20
ball = pygame.image.load("intro_ball.gif")
ball = pygame.transform.scale(ball, (ballSize, ballSize))
ballrect = ball.get_rect()
space_pressed = False
up_pressed=False
down_pressed=False
ball_moving = True
background_color = backgroundColor
score2=0


rectHeight = 75
rectWidth = 5
rectX = width-75
rectY = height/2
rectPos = [rectX, rectY, rectWidth, rectHeight]
recta = pygame.draw.rect(screen, paddleColor, rectPos, 0)
rectY2=height/2
rectX2 = (width-rectX)-rectWidth
rectPos2 = [rectX2, rectY, rectWidth, rectHeight]
recta2 = pygame.draw.rect(screen, paddleColor, rectPos, 0)

GameClock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)
score = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

  #      if event.type == pygame.KEYDOWN and pygame.K_SPACE and space_pressed == False:
  #          space_pressed = True
  #      if space_pressed and event.type == pygame.KEYUP:
  #          space_pressed = False
   # if space_pressed:
   #     if ball_moving:
  #          ball_speed_curr = speed[:]
   #         speed[0] = 0
 #           speed[1] = 0
  #          ball_moving = False
   #     else:
  #          speed = ball_speed_curr[:]
  #          ball_moving = True
  #      space_pressed = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and rectY>0:
        rectY = rectY - paddleSpeed
    if pressed[pygame.K_DOWN] and (rectY+rectHeight)<height:
        rectY = rectY + paddleSpeed

    GameClock.tick(GameSpeed)

    if pressed[pygame.K_w] and rectY2>0:
        rectY2 = rectY2 - paddleSpeed
    if pressed[pygame.K_s] and (rectY2+rectHeight)<height:
        rectY2 = rectY2 + paddleSpeed
    ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width or ((ballrect.right >= rectX) and (ballrect.right <= rectX + rectWidth) and overlap((rectY+rectHeight),rectY,ballrect.bottom,ballrect.top) ):
    #    speed[0] = -speed[0]

    if pygame.Rect.colliderect(recta, ballrect):
        speed[0] = -speed[0]

    if pygame.Rect.colliderect(recta2, ballrect):
        speed[0] = -speed[0]

    if ballrect.left < 0:
        speed[0] = -speed[0]
        score2 += 1
        resetBall()
    if ballrect.right > size[0]:
        speed[0] = -speed[0]
        score += 1
        resetBall()

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background_color)
    screen.blit(ball, ballrect)
    screen.blit(font.render('Player 1 Score: ' + str(score), True, textColor), (20, 20))
    screen.blit(font.render('Player 2 Score: ' + str(score2), True, textColor), (500, 20))

    rectPos = [rectX, rectY, rectWidth, rectHeight]
    recta = pygame.draw.rect(screen, paddleColor, rectPos, 0)
    rectPos2 = [rectX2, rectY2, rectWidth, rectHeight]
    recta2 = pygame.draw.rect(screen, paddleColor, rectPos2, 0)
    pygame.display.flip()
pygame.quit()
