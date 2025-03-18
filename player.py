import pygame
from constants import (
    PLAYER_MOVE_SPEED,
    PLAYER_RADIUS,
    PLAYER_ROTATION_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_COLOR,
)
from shot import Shot
from triangleshape import TriangleShape


class Player(TriangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS, PLAYER_COLOR, PLAYER_ROTATION_SPEED)
        self.shoot_timer = 0

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt * direction

    def update(self, dt):
        self.shoot_timer -= dt

        is_forward = 1

        keys = pygame.key.get_pressed()
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
        front_vertex = self.calculate_vertices()[0]
        shot = Shot(front_vertex.x, front_vertex.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
