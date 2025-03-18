import math
import pygame

from constants import PLAYER_COLOR


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
        vertices = []
        front_angle = math.radians(0 + self.rotation)
        front_vertex = self.position + pygame.Vector2(
            math.cos(front_angle) * self.radius,
            math.sin(front_angle) * self.radius,
        )
        vertices.append(front_vertex)

        back_angles = [120, 240]
        for angle in back_angles:
            radian_angle = math.radians(angle + self.rotation)
            back_vertex = self.position + pygame.Vector2(
                math.cos(radian_angle) * self.radius * 0.7,
                math.sin(radian_angle) * self.radius * 0.7,
            )
            vertices.append(back_vertex)

        return vertices

    def draw(self, screen):
        vertices = self.calculate_vertices()
        pygame.draw.polygon(screen, PLAYER_COLOR, vertices, width=2)
