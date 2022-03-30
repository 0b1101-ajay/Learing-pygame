import pygame
import sys
import random
from pygame.locals import *

pygame.init()

DISPLAY_SURF = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Shooter')
clock = pygame.time.Clock()

wood_bg = pygame.image.load('Shooting Range assets/Wood_BG.png')
land_bg = pygame.image.load('Shooting Range assets/Land_BG.png')
water_bg = pygame.image.load('Shooting Range assets/Water_BG.png')
cloud1 = pygame.image.load('Shooting Range assets/Cloud1.png')
cloud2 = pygame.image.load('Shooting Range assets/Cloud2.png')
crosshair = pygame.image.load('Shooting Range assets/crosshair.png')
duck_surface = pygame.image.load('Shooting Range assets/duck.png')

land_pos_Y = 560
land_speed = 1
water_pos_Y = 600
water_speed = 0.5
duck_list = []
for duck in range(20):
    duck_pos_X = random.randrange(50, 1200)
    duck_pos_Y = random.randrange(120, 600)
    duck_rect = duck_surface.get_rect(center=(duck_pos_X, duck_pos_Y))
    duck_list.append(duck_rect)

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)

    DISPLAY_SURF.blit(wood_bg, (0, 0))
    if land_pos_Y <= 520 or land_pos_Y >= 620:
        land_speed *= -1
    land_pos_Y -= land_speed

    if water_pos_Y <= 600 or water_pos_Y >= 650:
        water_speed *= -1
    water_pos_Y -= water_speed

    DISPLAY_SURF.blit(land_bg, (0, land_pos_Y))
    DISPLAY_SURF.blit(water_bg, (0, water_pos_Y))

    for duck_rect in duck_list:
        DISPLAY_SURF.blit(duck_surface, duck_rect)
        
    DISPLAY_SURF.blit(crosshair, crosshair_rect)
    DISPLAY_SURF.blit(cloud1, (100, 20))
    DISPLAY_SURF.blit(cloud2, (200, 20))
    DISPLAY_SURF.blit(cloud1, (500, 20))
    DISPLAY_SURF.blit(cloud2, (650, 20))
    DISPLAY_SURF.blit(cloud1, (1000, 20))

    pygame.display.update()
    clock.tick(120)
