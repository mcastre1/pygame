import pygame
from settings import *
from gameState import GameState

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Sprite groups
head_group = pygame.sprite.Group()
body_group = pygame.sprite.Group()
pickup_group = pygame.sprite.Group()

game_state = GameState(head_group, body_group, pickup_group, screen)

while True:
    game_state.state_manager()
    clock.tick(30)