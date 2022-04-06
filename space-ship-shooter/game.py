import pygame
import sys
import random
from pygame.locals import *


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.shield_surface = pygame.image.load('Meteor Dodger Assets/shield.png')
        self.health = 5

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constraint()
        self.display_health()

    def screen_constraint(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720

    def display_health(self):
        for index, shield in enumerate(range(self.health)):
            DISPLAY_SURF.blit(self.shield_surface, (index * 40 + 10, 10))

    def get_damage(self, damage_amount):
        self.health -= damage_amount


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

        if self.rect.centery >= 800:
            self.kill()


class Laser(pygame.sprite.Sprite):
    def __init__(self, path, pos, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -100:
            self.kill()

def main_game():
    laser_group.draw(DISPLAY_SURF)
    spaceship_group.draw(DISPLAY_SURF)
    meteor_group.draw(DISPLAY_SURF)

    laser_group.update()
    spaceship_group.update()
    meteor_group.update(1, 1)

    # collision
    if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
        spaceship_group.sprite.get_damage(1)

    for laser in laser_group:
        pygame.sprite.spritecollide(laser, meteor_group, True)

def end_game():
    text_surface = game_font.render('Game Over', True, (200, 170, 130))
    text_rect = text_surface.get_rect(centre = (600, 1000))
    DISPLAY_SURF.blit(text_surface,text_rect)

pygame.init()

DISPLAY_SURF = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Space Ship Shooter')
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40)

spaceship = SpaceShip('Meteor Dodger Assets/spaceship.png', 640, 500, 2)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

laser_group = pygame.sprite.Group()

meteor_group = pygame.sprite.Group()
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, 250)

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == METEOR_EVENT:
            meteor_path = random.choice(('Meteor Dodger Assets/Meteor1.png', 'Meteor Dodger Assets/Meteor2.png',
                                         'Meteor Dodger Assets/Meteor3.png'))
            random_xpos = random.randrange(0, 1280)
            random_ypos = random.randrange(-500, -50)
            random_xspeed = random.randrange(-1, 1)
            random_yspeed = random.randrange(4, 10)
            meteor = Meteor(meteor_path, random_xpos, random_ypos, random_xspeed, random_yspeed)
            meteor_group.add(meteor)

        if event.type == pygame.MOUSEBUTTONDOWN:
            new_laser = Laser('Meteor Dodger Assets/Laser.png', event.pos, 5)
            laser_group.add(new_laser)

    DISPLAY_SURF.fill((80, 125, 230))
    if spaceship_group.sprite.health > 0:
        main_game()

    else:
        end_game()


    pygame.display.update()
    clock.tick(120)

