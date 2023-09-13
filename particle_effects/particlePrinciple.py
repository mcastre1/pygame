import pygame, sys, random

class ParticlePrinciple:
    def __init__(self):
        self.particles = []
        self.screen = pygame.display.get_surface()

    # moves and draws particles
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                # move
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                # shrink
                particle[1] -= 0.2
                # draw a cirlce around the particle
                pygame.draw.circle(self.screen, pygame.Color('white'), particle[0], int(particle[1]))

    # adds particles
    def add_particles(self):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]
        radius = 10
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3,3)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)

    # delete particles after a certain time
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy