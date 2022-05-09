from turtle import left, update
from numpy import angle
import pygame
import GameObjects as GO

pygame.init()
HEIGHT = 1020
WIDTH = 1920
surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FRAME_RATE = 60
playing = True
SCALE = 16
pygame.display.set_caption("Ty and The Fight for Color")
BG = pygame.image.load("Characters/Orian.png").convert_alpha()
BG = pygame.transform.scale(BG, (BG.get_width() * 1,BG.get_height() * 1))
BGX = 0
BGX2 = BG.get_width()
Ty = GO.Player(960//SCALE, 510//SCALE, health=10, scale=SCALE)
TyFighter = GO.Spaceship(940//SCALE, 510//SCALE, health=10, scale=1)
image_angle = 0
newSurface = surface
X = False
mx, my = pygame.display.get_window_size()
img_copy = TyFighter.image
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
curDir = UP
offsetX = 0
offsetY = 0
moveSpeed = 10
run = True
speed = 60  # NEW
BGMovementSpeed = 20
def redrawWindow():
    surface.blit(BG, (BGX, 0))  # draws our first bg image
    surface.blit(BG, (BGX2, 0))  # draws the second bg image
    #pygame.display.update()  # updates the screen

while playing:
    # Get User Input(No AI Just People)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        img_copy = TyFighter.update(surface, Events, 0)
        curDir = RIGHT
    if keys[pygame.K_a]:
        img_copy = TyFighter.update(surface, Events, 180)
        curDir = LEFT
    if keys[pygame.K_s]:
        img_copy = TyFighter.update(surface, Events, -90)
        curDir = DOWN
    if keys[pygame.K_w]:
        img_copy = TyFighter.update(surface, Events, 90)
        curDir = UP
    if keys[pygame.K_SPACE]:
        if curDir == DOWN:
            offsetY += moveSpeed
        elif curDir == RIGHT:
            offsetX += moveSpeed
            BGX -= BGMovementSpeed
            BGX2 -= BGMovementSpeed
        elif curDir == LEFT:
            offsetX -= moveSpeed
            BGX += BGMovementSpeed
            BGX2 += BGMovementSpeed
        elif curDir == UP:
            offsetY -= moveSpeed
    if keys[pygame.K_LSHIFT]:
    #Check Previose project for collision box   
        pass

    if BGX < BG.get_width() * -1:  # If our bg is at the -width then reset its position
        BGX = BG.get_width()
    
    if BGX2 < BG.get_width() * -1:
        BGX2 = BG.get_width()
    # The Great Loop O' Event
    Events = pygame.event.get()
    for event in Events:
        if event.type == pygame.QUIT or X == True:
            playing = False
    # Update Screen
    surface.blit(BG, (0 * SCALE, 0 * SCALE))
    redrawWindow()
    surface.blit(img_copy, ((mx/2 + offsetX) - int(img_copy.get_width() / 2), (my/2 + offsetY) - int(img_copy.get_height() / 2)))    
    pygame.display.update()
    clock.tick(FRAME_RATE)

pygame.quit()