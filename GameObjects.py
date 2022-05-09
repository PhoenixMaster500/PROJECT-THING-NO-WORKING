
from email.mime import image
from turtle import position
from numpy import angle
import pygame
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, health=10, scale=1, image="Characters/Ty.png"):
        self.SIZE = 16
        self.x = x
        self.y = y
        self.health = health
        self.scale = scale
        self.image = pygame.image.load("Characters/Ty.png").convert_alpha()
        #Transformers
        self.image = pygame.transform.scale(self.image, (self.SIZE * self.scale, self.SIZE * self.scale))
        
    def update(self, surface, Events):
        surface.blit(self.image, (self.x * self.scale, self.y * self.scale))

class Spaceship:
    def __init__(self, x, y, health=10, scale=1, image="Characters/The-Tyfighter2.png"):
        self.image = pygame.image.load(image).convert_alpha()
        self.SIZE = self.image.get_width()
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (self.SIZE * self.scale, self.SIZE * self.scale))
        self.x = x
        self.y = y
        self.health = health
        #Past Here is Complacated STUFF DO NOT TRESPASS
        self.theta = 0
        self.omega = 0
        self.v = 0
        self.torque = 0
        self.force = 0
        self.MASS = 1
        self.DRAG = 1
        self.TORQUE_MAG = 1
        self.FORCE_MAG = 1
        self.originX = self.image.get_size()[0]
        self.originY = self.image.get_size()[1]

    def update(self, surface, Events, image_angle):
        #Makes Image Point Right
        image_angle += -90
        img_copy = pygame.transform.rotate(self.image, image_angle)
        return img_copy
