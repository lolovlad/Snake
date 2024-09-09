from abc import ABC, abstractmethod
from pygame.math import Vector2


class GabeObject(ABC):
    def __init__(self, x: int, y: int, size: int):
        self._x: int = x
        self._y: int = y
        self._size: int = size
        self._normal: Vector2 = Vector2(0, 0)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @abstractmethod
    def render(self, *args, **kwargs):
        pass


