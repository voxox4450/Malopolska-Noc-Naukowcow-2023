from const import *

class Game:
    def __init__(self) -> None:
        self.list_BG = []
        self.index = 0
        self.points = 0
        self.font_lives = pygame.font.SysFont("Berlin Sans FB Demi", 50)

    def change_bg(self, lists: list) -> None:
        self.index += 1
        self.index %= len(lists)
        self.list_BG = lists[self.index]

    def draw_points(self, surface: object) -> None:
        if self.points > 9:
            self.points = 1
        text = self.font_lives.render(f'Punkty: {self.points}/9', True, YELLOW)
        surface.blit(text, (20, 10))
