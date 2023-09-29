from const import *


class TextInput:
    def __init__(self, x: int, y: int, width: int, height: int, place: str) -> None:
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Arial Black", 40)
        self.text = ''
        self.place = place
        self.helping_2 = False
        self.place_font = pygame.font.Font.render(self.font, place, True, (100, 100, 100))


    def tick(self, events) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_SPACE:
                    self.text = ''
                else:
                    self.text += event.unicode


    def draw(self, screen: object, planet: int) -> None:
        pygame.draw.rect(screen, (4, 207, 222), (self.x_cord - 5, self.y_cord - 5, self.width + 10, self.height + 10), border_radius=30)
        pygame.draw.rect(screen, (255, 255, 255), (self.x_cord, self.y_cord, self.width, self.height), border_radius=30)

        if self.text and not self.helping_2:
            font_image = pygame.font.Font.render(self.font, self.text, False, (0, 0, 0))
            screen.blit(font_image, (self.x_cord + 10, self.y_cord + 5))
        elif self.helping_2 or self.text:
            font_helping = pygame.font.Font.render(self.font, planet_names[planet][0], False, (0, 0, 0))
            screen.blit(font_helping, (self.x_cord + 10, self.y_cord + 5))
            font_image = pygame.font.Font.render(self.font, self.text, False, (0, 0, 0))
            screen.blit(font_image, (self.x_cord + 10, self.y_cord + 5))
        else:
            screen.blit(self.place_font, (self.x_cord + 10, self.y_cord + 5))
