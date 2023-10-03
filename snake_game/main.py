import pygame
from settings import *
from gameState import GameState

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Snake Game')

#sounds
apple_bite_sfx = pygame.mixer.Sound('./snake_game/sounds/apple_bite.ogg')
#music
background_music = pygame.mixer.Sound('./snake_game/sounds/background_music.mp3')
background_music.play(-1)

# Sprite groups
head_group = pygame.sprite.Group()
body_group = pygame.sprite.Group()
pickup_group = pygame.sprite.Group()

game_state = GameState(head_group, body_group, pickup_group, screen, apple_bite_sfx, background_music)
game_state.set_state('intro')

while True:
    game_state.state_manager()
    pygame.display.update()
    clock.tick(30)
    