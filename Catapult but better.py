import pygame
import sys

#Defining Variables
SCREEN_SIZE = WIDTH, HEIGHT = (1366, 768)
BLACK = (0, 0, 0)
BASED = (10, 156, 247)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 15
SQUARE_RADIUS = 30
rect_dmns = (30, 30)
handled = False
font = pygame.font.Font('comicsansms.ttf', 32)
text = font.render('Press Space to unpause and Esc to Quit', True, green, blue)

time = 1
ball_spey = int(384)
ball_spex = int(240)
ball_accy = int(-15)
ball_accx = int(1)
ball_posy = 0
ball_posx = 0
touched_grass = 0
screen_x = 1366
screen_y = 768

# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Catapulting Spheres')
fps = pygame.time.Clock()
paused = False

# Ball setup
ball_pos = [int(50), int(240)]

#Ball defining
def update():
    ball_posy = ball_spey + (ball_accy + time)
    ball_posx = ball_spex + (ball_accx + time)
    ball_pos[1] = ball_posy
    ball_pos[0] = ball_posx
    
    #print(3)
    #print("updated")
    #print(ball_spey)
    #print(ball_spex)

def render():
    screen.fill(BLACK)
    pygame.draw.circle(screen, BASED, ball_pos, CIRCLE_RADIUS, 0)
    pygame.draw.rect(screen, RED, rect_dmns)
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
        update()
        if ball_pos[1] >= 381:
            ball_accy = 0 - (time + 1)
            touched_grass = touched_grass + 1
        if ball_pos[0] >= 1366:
            ball_accx = 0 - (time + 1)
            pygame.quit()
            sys.exit()
        time = time + 1
        render()
        if touched_grass == 1:
            print(ball_pos[0])
        ball_spex = ball_pos[0]
        ball_spey = ball_pos[1]
        
