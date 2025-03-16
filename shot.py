import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        color = (45, 226, 0) 
        pygame.draw.circle(screen, color, self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
