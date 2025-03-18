import pygame


class TriangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, rotation_speed):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.radius = radius
        self.color = color
        self.rotation_speed = rotation_speed

    def calculate_vertices(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius * 0.7
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt, direction):
        self.rotation += self.rotation_speed * dt * direction

    def draw(self, screen):
        vertices = self.calculate_vertices()
        pygame.draw.polygon(screen, self.color, vertices, width=2)

    # nice way to create a triangle
    # def calculate_vertices(self):
    #     vertices = []
    #     front_angle = math.radians(0 + self.rotation)
    #     front_vertex = self.position + pygame.Vector2(
    #         math.cos(front_angle) * self.radius,
    #         math.sin(front_angle) * self.radius,
    #     )
    #     vertices.append(front_vertex)
    #
    #     back_angles = [120, 240]
    #     for angle in back_angles:
    #         radian_angle = math.radians(angle + self.rotation)
    #         back_vertex = self.position + pygame.Vector2(
    #             math.cos(radian_angle) * self.radius * 0.7,
    #             math.sin(radian_angle) * self.radius * 0.7,
    #         )
    #         vertices.append(back_vertex)
    #
    #     return vertices
