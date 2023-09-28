import pygame, random
from settings import *

class Particle:
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
                pygame.draw.rect(self.screen, pygame.Color(RED), (particle[0][0], particle[0][1], 7, 7))

    # adds particles
    def add_particles(self, topleft_x, topleft_y):
        for x in range(random.randint(5, 8)):
            for y in range(random.randint(5, 8)):
                pos_x = topleft_x + x
                pos_y = topleft_y + y
                frames = random.randint(0, 15)
                direction_x = random.randint(-3,3)
                direction_y = random.randint(-3,3)
                particle = [[pos_x, pos_y], frames, [direction_x, direction_y]]
                self.particles.append(particle)

    # delete particles after a certain time
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy