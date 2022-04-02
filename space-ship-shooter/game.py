import pygame
import sys
import random
from pygame.locals import *


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constraint()

    def screen_constraint(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720


class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self, x_speed, y_speed):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed


pygame.init()

DISPLAY_SURF = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Space Ship Shooter')
clock = pygame.time.Clock()

spaceship = SpaceShip('Meteor Dodger Assets/spaceship.png', 640, 500, 2)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor = Meteor('Meteor Dodger Assets/Meteor1.png', 100, 100, 2, 2)
meteor_group = pygame.sprite.Group()
meteor_group.add(meteor)

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY_SURF.fill((80, 125, 230))
    spaceship_group.draw(DISPLAY_SURF)
    meteor_group.draw(DISPLAY_SURF)
    spaceship_group.update()
    meteor_group.update(1, 1)
    pygame.display.update()
    clock.tick(120)
