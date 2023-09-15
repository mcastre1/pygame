import pygame, sys, random

class NyanParticlePrinciple:
    def __init__(self):
        self.particles = []
        self.screen = pygame.display.get_surface()

    # moves and draws particles
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                # move
                particle[0][0] -= 1

                # draw a cirlce around the particle
                #pygame.draw.circle(self.screen, pygame.Color('white'), particle[0], int(particle[1]))
                rect = pygame.Rect(particle[0][0] - 20, particle[0][1] + particle[1], 10, 10)
                pygame.draw.rect(self.screen, particle[2], rect)


    # adds particles
    def add_particles(self, offset, color):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]

        particle_rect = [[pos_x, pos_y], offset, color]
        self.particles.append(particle_rect)

    # delete particles after a certain time
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[0][0] > 0]
        self.particles = particle_copy
        print(len(self.particles))