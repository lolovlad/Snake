import pygame
from random import randrange
from settings import RES, SIZE, FPS, VECTORS_MOVE

from Snake import Snake
from Apple import Apple

#RES = 800
#SIZE = 50

#x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
#apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

#dirs = {'W': True, 'S': True, 'A': True, 'D': True}

#length = 1
#snake = [(x, y)]
#dx, dy = 0, 0
#fps = 10


pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

snake = Snake(
    randrange(0, RES, SIZE),
    randrange(0, RES, SIZE),
)
snake.init()

apple = Apple(
    randrange(0, RES, SIZE),
    randrange(0, RES, SIZE),
    "red"
)

while True:
    sc.fill(pygame.Color('black'))

    snake.render(sc)
    apple.render(sc)

    snake.move()

    if snake.is_collision_snake():
        break

    if apple.collision(snake.snake_head):
        apple.move(
            randrange(0, RES, SIZE),
            randrange(0, RES, SIZE)
        )
        snake.add_snake()
        FPS += 1

    if snake.snake_head.x < 0:
        snake.spaw(RES, snake.y)
    elif snake.snake_head.x > RES - SIZE:
        snake.spaw(0, snake.y)
    elif snake.snake_head.y < 0:
        snake.spaw(snake.x, RES)
    elif snake.snake_head.y > RES - SIZE:
        snake.spaw(snake.x, 0)

    pygame.display.flip()
    clock.tick(FPS)

    to_move = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        to_move = VECTORS_MOVE[pygame.K_w]
    if keys[pygame.K_s]:
        to_move = VECTORS_MOVE[pygame.K_s]
    if keys[pygame.K_a]:
        to_move = VECTORS_MOVE[pygame.K_a]
    if keys[pygame.K_d]:
        to_move = VECTORS_MOVE[pygame.K_d]

    if to_move is not None:
        if to_move + snake.vector != pygame.Vector2(0, 0):
            snake.vector = to_move
