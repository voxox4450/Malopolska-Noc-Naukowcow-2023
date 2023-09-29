import pygame
from numbers import Real


class Button:
    def __init__(self, x: int, y: int, on: object, off: object, scale: float) -> None:
        self.x = x
        self.y = y
        self.on = on
        self.off = off
        self.img = on
        self.scale = scale
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.image_1 = pygame.transform.scale(on, (int(self.width * scale), int(self.height * scale)))
        self.image_2 = pygame.transform.scale(off, (int(self.width * scale), int(self.height * scale)))
        self.clicked = True

    def draw(self, surface: object) -> None:
        if self.clicked:
            surface.blit(self.image_1, (self.x, self.y))
        else:
            surface.blit(self.image_2, (self.x, self.y))

    def click(self, x1: Real, y1: Real) -> bool:
        if self.x <= x1 <= self.x + self.width * self.scale:
            if self.y <= y1 <= self.y + self.height * self.scale:
                return True
        return False
