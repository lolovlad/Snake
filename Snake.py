from SnakeObject import SnakeObject
from GameObjcet import GabeObject
from pygame.math import Vector2
from settings import SIZE

from pygame import Surface


class Snake(GabeObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 1)
        self.__snake: list[SnakeObject] = []
        self._normal = Vector2(1, 0)

    @property
    def vector(self) -> Vector2:
        return self._normal

    @property
    def snake_head(self):
        return self.__snake[-1]

    @vector.setter
    def vector(self, vector: Vector2):
        self._normal = vector

    def __add_new_snake_object(self):
        self.__snake.append(SnakeObject(
            self._x,
            self._y,
            SIZE,
            'green'
        ))

    def init(self):
        self.__add_new_snake_object()

    def add_snake(self):
        self.__snake.append(SnakeObject(
            self._x,
            self._y,
            SIZE,
            'green'
        ))

    def move(self):
        self._x += SIZE * self._normal.x
        self._y += SIZE * self._normal.y
        self.__snake.pop(0)
        self.__add_new_snake_object()

    def render(self, sc: Surface):
        for i in self.__snake:
            i.render(sc)

    def spaw(self, x: int, y: int):
        self._x = x
        self._y = y

    def is_collision_snake(self) -> bool:
        is_collision = False
        for i in self.__snake[:-1]:
            if i.y == self.snake_head.y and i.x == self.snake_head.x:
                is_collision = True
                return is_collision
        return is_collision
