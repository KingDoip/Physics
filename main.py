import pygame
import sys
import random

#Defining Variables
SCREEN_SIZE = WIDTH, HEIGHT = (800, 600)
BLACK = (0, 0, 0)
BASED = (10, 156, 247)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 15
SQUARE_RADIUS = 30
rect_wi = int(random.randrange(int(WIDTH / 3), int(WIDTH / 2)))
rect_hi = int(HEIGHT / 2)
rect_dmns = (rect_wi, rect_hi, 50, 50)
handled = False
pygame.font.init()
font = pygame.font.Font('comicneueregular.ttf', 32)
text = font.render('Press Space to unpause and Esc to Quit', True, GREEN, BLACK)
time = 1
ball_spey = int(3)
ball_spex = int(2)
ball_accy = int(-15)
ball_accx = int(1)
ball_posy = int(HEIGHT) / 2
ball_posx = int(0)
touched_grass = 0
Loop = 0
rect_color = RED
Pog = 0

# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Catapulting Balls')
fps = pygame.time.Clock()
paused = False

# Ball setup
ball_pos = [int(0), int(HEIGHT) / 2]


#Ball defining
def update():
  if isinstance((int(Loop) / 2), float) == True:
    if Loop == 1:
      globals()['ball_accy2'] = globals()['ball_accy']
      globals()['ball_accx2'] = globals()['ball_accx']
      globals()['ball_spex2'] = globals()['ball_spex']
      globals()['ball_spey2'] = globals()['ball_spey']
    ball_spey = globals()['ball_spey2'] + (globals()['ball_accy2'] + time)
    ball_spex = globals()['ball_spex2'] + (globals()['ball_accx2'] + time)
    ball_posy = ball_pos[1] + ball_spey
    ball_posx = ball_pos[0] + ball_spex
    ball_pos[1] = ball_posy
    ball_pos[0] = ball_posx
  else:
    ball_spey2 = ball_spey + (ball_accy + time)
    ball_spex2 = ball_spex + (ball_accx + time)
    ball_posy2 = ball_pos[1] + ball_spey2
    ball_posx2 = ball_pos[0] + ball_spex2
    ball_pos[1] = ball_posy2
    ball_pos[0] = ball_posx2
    
    #print(3)
    #print("updated")
    #print(ball_spey)
    #print(ball_spex)


def render():
    screen.fill(BLACK)
    pygame.draw.circle(screen, BASED, ball_pos, CIRCLE_RADIUS, 0)
    pygame.draw.rect(screen, rect_color, rect_dmns)
    pygame.display.update()
    fps.tick(10)


#Ball generating

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                paused = not paused
    if not paused:
        Loop = Loop + 1
        render()
        update()
        if ball_pos[1] >= (HEIGHT / 2):
            ball_accy = 0 - (time + 1)
            touched_grass = touched_grass + 1
        if ball_pos[0] >= WIDTH:
            ball_accx = 0 - (time + 1)
            pygame.quit()
            sys.exit()
        if ball_pos[0] >= (rect_wi - 25):
          if (rect_wi + 25) >= ball_pos[0]:
            print("wi")
            if ball_pos[1] >= (rect_hi - 15):
              if (rect_hi + 15) >= ball_pos[1]:
                Pog = 1
                print("hi")
        if Pog == 1:
          rect_color = GREEN
          
        time = time + 1
        if touched_grass == 1:
            print(ball_pos[0])
            print(ball_pos[1])
            print(Pog)
            print(rect_wi)
            print(rect_hi)
        ball_spex = ball_pos[0]
        ball_spey = ball_pos[1]
