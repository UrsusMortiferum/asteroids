import pygame
from constants import PLAYER_MOVE_SPEED, PLAYER_RADIUS, PLAYER_ROTATION_SPEED
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
        
    def rotate(self, dt, direction):
        self.rotation += PLAYER_ROTATION_SPEED * dt * direction

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt * direction

    def update(self, dt):
        keys = pygame.key.get_pressed()
        direction = 1
        if keys[pygame.K_s]:
            direction = -1

        if keys[pygame.K_w]:
            self.move(dt, direction)
        if keys[pygame.K_s]:
            self.move(dt, direction)
        if keys[pygame.K_a]:
            self.rotate(-dt, direction)
        if keys[pygame.K_d]:
            self.rotate(dt, direction)
