import math
import pygame


class TriangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.radius = radius

    def calculate_vertices(self):
        angles = [0, 120, 240]
        vertices = []
        for angle in angles:
            radian_angle = math.radians(angle + self.rotation)
            vertex = self.position + pygame.Vector2(
                math.cos(radian_angle) * self.radius,
                math.sin(radian_angle) * self.radius,
            )
            vertices.append(vertex)
        return vertices

    def draw(self, screen):
        vertices = self.calculate_vertices()
        pygame.draw.polygon(screen, PLAYER_COLOR, vertices)
