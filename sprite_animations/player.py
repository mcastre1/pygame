import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        # self.image = pygame.Surface([20, 20])
        # self.image.fill((255,255,255))
        # self.rect = self.image.get_rect()
        # self.rect.topleft = [pos_x, pos_y]

        self.sprites = []
        self.is_animating = False
        for n in range(1,11):
            self.sprites.append(pygame.image.load(f'./graphics/attack_{n}.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    
    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            # self.current_sprite += 1
            self.current_sprite += .2 # Slows down animation by converting this number to int, below
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]