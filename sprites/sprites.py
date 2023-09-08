import pygame
import sys
from crosshair import Crosshair
from target import Target
import random

pygame.init()

screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

background = pygame.image.load('./sprites/graphics/BG.png')


crosshair = Crosshair('./sprites/graphics/crosshair.png')

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

pygame.mouse.set_visible(False)

# Targets
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('./sprites/graphics/target.png', random.randrange(0,screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()


    pygame.display.flip()
    #screen.blit(background,(0,0))
    screen.fill((255,255,255))
    target_group.draw(screen)

    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
            