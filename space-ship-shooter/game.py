import pygame
import sys
import random
from pygame.locals import *


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


pygame.init()

DISPLAY_SURF = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Space Ship Shooter')
clock = pygame.time.Clock()

spaceship = SpaceShip('Meteor Dodger Assets/spaceship.png', 640, 500, 2)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    spaceship_group.draw(DISPLAY_SURF)
    pygame.display.update()
    clock.tick(120)
