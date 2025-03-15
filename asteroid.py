import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = (255, 78, 10)
        pygame.draw.circle(screen, color, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
