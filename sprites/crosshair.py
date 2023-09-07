import pygame

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sount('gunshot.wav')

    def shoot(self):
        self.gunshot.play()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
