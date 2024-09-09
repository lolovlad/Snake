from GameObjcet import GabeObject

from settings import SIZE
from pygame import draw, Surface, Color


class Apple(GabeObject):
    def __init__(self, x: int, y: int, color: str):
        super().__init__(x, y, SIZE)
        self.__color: str = color

    def render(self, sc: Surface):
        draw.rect(sc, Color(self.__color), (self._x, self._y, self._size, self._size))

    def move(self, x: int, y: int):
        self._x = x
        self._y = y

    def collision(self, obj: GabeObject) -> bool:
        return self._x == obj.x and self._y == obj.y
