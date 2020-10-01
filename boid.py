from pygame import Vector2 as Vector; from pygame.color import Color
from random import randint, choice
import numpy as np
from settings import *
import copy

COLORS = {
    "tomato" : (231, 76, 60 ),
    "salmon" : (236, 112, 99),
    "smoked" : ( 203, 67, 53 )
}



class Boid:

    def __init__(self, x, y):

        self.velocity = Vector( *((np.random.rand(2))*3) )
        self.position = Vector(x, y)

        self.view_radius = 100

        random_hue = randint(0,360)
        self.color = Color(0,0,0); self.color.hsla = (random_hue, 100, 75, 1)
        self.original_color = Color(0,0,0); self.original_color.hsla = (random_hue, 100, 75, 1)


    
    def separation(self, boids):
        
        c = Vector(0, 0)

        for b in boids:

            if b != self:
                if np.linalg.norm(b.position - self.position) < self.view_radius*0.6:

                    c -= (b.position - self.position)
        
        return c

    def alignment(self, boids):

        # perceived velocity
        pvj = Vector(0,0)
        total = 1

        for b in boids:
            if b != self:
                    pvj += b.velocity
                    total += 1
        
        pvj /= total

        return (pvj - self.velocity) / 8

    def cohesion(self, boids):

        pcj = Vector(0,0)

        for b in boids:
            if b != self:
                pcj += b.position
        
        if len(boids)-1 > 0:
            pcj /= len(boids) - 1
        
        return (pcj - self.position) / 100

    def near_boids(self, boids):

        near = []

        for b in boids:
            if np.linalg.norm(b.position - self.position) < self.view_radius:
                near.append(b)

        return near

    def normalize_velocity(self):
        
        if np.linalg.norm(self.velocity) > MAX_VELOCITY:
            self.velocity *= 0.7

    def teleport(self):
        
        if self.position.x > WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIDTH
        
        if self.position.y > HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = HEIGHT

    def coloration(self, boids):

        hue_avg = np.mean( [x.color.hsla[0] for x in boids] )

        hue_current = self.color.hsla[0]

        if (len(boids) < 5):
            hue_avg = self.original_color.hsla[0]

        hue_dist = hue_avg - hue_current

        hue_adjust = hue_dist / 100

        self.color.hsla = (self.color.hsla[0] + hue_adjust, self.color.hsla[1], self.color.hsla[2], self.color.hsla[3])

    def bird_orientation_and_positions(self):
        boid = self
        degree = np.arctan2(boid.velocity.y, boid.velocity.x)

        triangle = [0, ((1 - BIRD_ANGLE) * np.pi), ((1 + BIRD_ANGLE) * np.pi)]
        radius = BIRD_SIZE
        result = []
        for t in triangle:
            # apply the circle formula
            x = boid.position.x + radius * np.cos(t + degree)
            y = boid.position.y + radius * np.sin(t + degree)
            result.append((x, y))
        return result

x = Boid(10,10)