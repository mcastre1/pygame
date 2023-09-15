import pygame, sys
from particlePrinciple import ParticlePrinciple
from nyan_particle import NyanParticlePrinciple

screen_width = 800
screen_height = 800
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_height))

particle1 = ParticlePrinciple()
particle2 = NyanParticlePrinciple()

# This is called every 40 milliseconds
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            #particle1.add_particles()
            particle2.add_particles(6)

    screen.fill((30,30,30))
    #particle1.emit()
    particle2.emit()
    pygame.display.flip()
    clock.tick(60)