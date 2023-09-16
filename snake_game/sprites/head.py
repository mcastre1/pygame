import pygame
from settings import *

class Head(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.center = (pos_x, pos_y)
        self.image.fill(GREEN)
        self.speed = SNAKE_SPEED
        self.direction = 'Right'

    def update(self):
        if self.direction == 'Right':
            self.pos_x += self.speed
        if self.direction == 'Left':
            self.pos_x -= self.speed
        if self.direction == 'Up':
            self.pos_y -= self.speed
        if self.direction == 'Down':
            self.pos_y += self.speed

        self.rect.center = (self.pos_x, self.pos_y)

    def set_direction(self, direction):
        self.direction = direction
        print(f'set direction to {self.direction}')

    def draw(self):
        pygame.display.get_surface().blit(self.image, self.rect)


    