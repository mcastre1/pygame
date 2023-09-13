import pygame

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
                particle[0][1] += particle[2]
                # shrink
                particle[1] -= 0.2
                # draw a cirlce around the particle
                pygame.draw.circle(self.screen, pygame.Color('white'), particle[0], int(particle[1]))

    # adds particles
    def add_particles(self):
        pos_x = 250
        pos_y = 250
        radius = 10
        direction = -3
        particle_circle = [[pos_x, pos_y], radius, direction]
        self.particles.append(particle_circle)

    # delete particles after a certain time
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy