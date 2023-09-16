import pygame, sys
from settings import *
from sprites.head import Head

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Sprites
head = Head(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Sprite groups
head_group = pygame.sprite.Group()
body_group = pygame.sprite.Group()
pickup_group = pygame.sprite.Group()

# Add sprites to groups
head_group.add(head)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    head_group.update()
    head_group.draw(screen)

    pygame.display.update()

    clock.tick(FPS)