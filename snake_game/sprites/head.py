import pygame
from settings import *

class Head(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE,SIZE))
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.center = (pos_x, pos_y)
        self.image.fill(GREEN)
        self.speed = SNAKE_SPEED
        self.direction = 'Right'
        self.score = 0

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

    # Method used to change direction of snake from main file
    def set_direction(self, direction):
        self.direction = direction

    def draw(self):
        pygame.display.get_surface().blit(self.image, self.rect)

    def add_score(self, score):
        self.score += score

    def get_score(self):
        return int(self.score)


    