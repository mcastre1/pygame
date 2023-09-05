import pygame
import sys
from crosshair import Crosshair

pygame.init()

screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

crosshair = Crosshair(50,50,100,100,(255,255,255))

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()


    pygame.display.flip()
    crosshair_group.draw(screen)
    clock.tick(60)
            