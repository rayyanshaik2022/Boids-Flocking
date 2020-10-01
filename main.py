import pygame
from settings import *
from boid import *
from random import randint

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self):
        
        self.boids = [Boid( randint(0,WIDTH), randint(0,HEIGHT) ) for i in range(POP_SIZE)]

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Controls update speed (FPS per second)
            self.events()
            self.draw_background()
            self.update()

            pygame.display.flip()

    def close(self):
        pygame.quit()
        quit()

    def update(self):
        
        for b in self.boids:

            nearby_boids = b.near_boids(self.boids)

            seperation = b.separation(self.boids) * 0.015
            alignment = b.alignment(nearby_boids) * 0.8
            cohesion = b.cohesion(nearby_boids) * 1

            b.velocity = b.velocity + seperation + alignment + cohesion
            b.position += b.velocity

            b.teleport()
            b.normalize_velocity()
            b.coloration(nearby_boids)
            
            pygame.draw.polygon(self.screen, b.color, b.bird_orientation_and_positions())

    def draw_background(self):
        self.screen.fill( (0, 6, 26) )


    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()


# create the game object
g = Game()
g.new()
g.run()