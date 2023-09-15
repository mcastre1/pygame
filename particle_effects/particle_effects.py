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
nyan_image = pygame.image.load('particle_effects/nyan_cat.png').convert_alpha()
nyan_rect = nyan_image.get_rect()

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
            particle2.add_particles(-30, 'Red')
            particle2.add_particles(-20, 'Orange')
            particle2.add_particles(-10, 'Yellow')
            particle2.add_particles(0, 'Green')
            particle2.add_particles(10, 'Blue')
            particle2.add_particles(20, 'Purple')

    screen.fill((30,30,30))
    #particle1.emit()
    particle2.emit()

    #Draw nyan cat picture
    nyan_rect.center=(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    screen.blit(nyan_image, nyan_rect)

    pygame.display.flip()
    clock.tick(60)