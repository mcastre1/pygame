import pygame

class Crosshair(pygame.sprite.Sprite):
    def __init__(self ,width ,height ,pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)