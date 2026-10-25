import pygame

import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
       self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        else:
            log_event("asteroid_split")
            new_vector = random.uniform(20, 50)
            asteroid1_vector = self.velocity.rotate(new_vector)
            asteroid2_vector = self.velocity.rotate(-new_vector)
            new_asteroid_1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_1.velocity = asteroid1_vector * 1.2
            new_asteroid_2.velocity = asteroid2_vector * 1.2
