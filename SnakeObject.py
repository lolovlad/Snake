from GameObjcet import GabeObject
import pygame


class SnakeObject(GabeObject):
    def __init__(self,
                 x: int,
                 y: int,
                 size: int,
                 color: str
                 ):
        super().__init__(x, y, size)
        self.__color: str = color

    def render(self, sc: pygame.Surface):
        pygame.draw.rect(sc, pygame.Color(self.__color), (self._x, self._y, self._size, self._size))

