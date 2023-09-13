import pygame, sys
from particlePrinciple import ParticlePrinciple

screen_width = 800
screen_height = 800
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_height))

particle1 = ParticlePrinciple()

# This is called every 40 milliseconds
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            particle1.add_particles()

    screen.fill((30,30,30))
    particle1.emit()
    pygame.display.flip()
    clock.tick(60)