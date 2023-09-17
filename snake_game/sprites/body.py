import pygame
from settings import *

class Body(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE,SIZE))
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.center = (self.pos_x, self.pos_y)
        self.direction = direction

    def update(self, pos_x, pos_y, direction):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction

        self.rect.center = (self.pos_x, self.pos_y)