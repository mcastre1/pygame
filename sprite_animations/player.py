import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]