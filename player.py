import pygame
from constants import (
    PLAYER_MOVE_SPEED,
    PLAYER_RADIUS,
    PLAYER_ROTATION_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from shot import Shot
from triangleshape import TriangleShape


# class Player(CircleShape):
#     def __init__(self, x, y):
#         super().__init__(x, y, PLAYER_RADIUS)
#         self.rotation = 0
#         self.shoot_timer = 0
#
#     def triangle(self):
#         forward = pygame.Vector2(0, 1).rotate(self.rotation)
#         right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
#         a = self.position + forward * self.radius
#         b = self.position - forward * self.radius - right
#         c = self.position - forward * self.radius + right
#         return [a, b, c]
#
#     def draw(self, screen):
#         pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), width=2)
#         pygame.draw.circle(screen, PLAYER_COLOR, self.position, self.radius, width=2)


class Player(TriangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shoot_timer = 0

    def rotate(self, dt, direction):
        self.rotation += PLAYER_ROTATION_SPEED * dt * direction

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt * direction

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        is_forward = 1
        if keys[pygame.K_s]:
            is_forward = -1

        if keys[pygame.K_w]:
            self.move(dt, is_forward)
        if keys[pygame.K_s]:
            self.move(dt, is_forward)
        if keys[pygame.K_a]:
            self.rotate(-dt, is_forward)
        if keys[pygame.K_d]:
            self.rotate(dt, is_forward)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
