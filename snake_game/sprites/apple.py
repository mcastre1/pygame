import pygame
from settings import *

class Apple(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.rect = self.image.get_rect()
        self.rgb = RED
        self.image.fill(self.rgb)

        self.rect.center = (pos_x, pos_y)