import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,800))

second_surface = pygame.Surface([100,200])
second_surface_rect = second_surface.get_rect()
second_surface.fill((0,0,255))

kitten = pygame.image.load('kitten.jpg')
kitten_rect = kitten.get_rect()
kitten_rect.topleft = [100,100]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))
    screen.blit(second_surface, (0,50))
    screen.blit(kitten, kitten_rect)
    kitten_rect.right += 3


    pygame.display.flip() # Draws everything in this loop cycle.
    clock.tick(60) # Frame rate, in this case 60 frames per second (FPS)