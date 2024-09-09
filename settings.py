import pygame
from pygame.math import Vector2

RES = 800
SIZE = 50
FPS = 5

VECTORS_MOVE = {
    pygame.K_w: Vector2(0, -1),
    pygame.K_s: Vector2(0, 1),
    pygame.K_a: Vector2(-1, 0),
    pygame.K_d: Vector2(1, 0),
}
