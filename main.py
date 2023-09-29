from game import Game
from const import *
from button import Button
from TextInput import TextInput


class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(225 * ' '+'Rozpoznaj planety')
        self.game = Game()
        self.points = self.game.points
        self.points_text = 0
        self.text_input = TextInput(WIDTH - 375, HEIGHT - 100, 350, 75, 'Nazwa planety')

        #wykorzystanie koła
        Kwyko = pygame.image.load('KR/x.png').convert_alpha()
        #podowiedz ustna
        Kustna = pygame.image.load('KR/on.png').convert_alpha()
        self.Kustna = Button(10, 770, Kustna, Kwyko, 0.4)
        #Kolory szarosci
        Kszarosc = pygame.image.load('KR/Kszarosci.png').convert_alpha()
        self.Kszarosc = Button(100, 770, Kszarosc, Kwyko, 0.4)
        #pierwsza litera
        Klitera = pygame.image.load('KR/pierwsza litera.png').convert_alpha()
        self.Klitera = Button(190, 770, Klitera, Kwyko, 0.4)
        self.click = False


    def run(self) -> None:
        run = True
        screen = self.screen
        game = self.game
        text_input = self.text_input
        content = None
        helping = False
        one = BGs
        two = BGs2

        helping_2 = False

        count1 = True
        count2 = True
        count3 = True

        while run:
            pos = pygame.mouse.get_pos()
            events = pygame.event.get()
            content = text_input.tick(events)
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if count1:
                        if self.Kustna.click(pos[0], pos[1]):
                            self.click = False
                            self.Kustna.clicked = self.click
                            count1 = False
                    else:
                        pass
                    if count2:
                        if self.Kszarosc.click(pos[0], pos[1]):
                            self.click = False
                            self.Kszarosc.clicked = self.click
                            count2 = False
                            helping = True
                    else:
                        pass
                    if count3:
                        if self.Klitera.click(pos[0], pos[1]):
                            self.click = False
                            self.Klitera.clicked = self.click
                            count3 = False
                            helping_2 = True
                    else:
                        pass

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if planet_names[game.index] == content:
                        game.points += 1
                        game.change_bg(BGs2)
                        print("Poprawnie")
                        helping = False
                        helping_2 = False
                        text_input.text = ''
                    else:
                        print("Wpisałeś błędną nazwę planety!!!")

            if not helping:
                self.draw(two)
            else:
                self.draw(one)
            self.Kustna.draw(screen)
            self.Kszarosc.draw(screen)
            self.Klitera.draw(screen)

            if not helping_2:
                text_input.draw(screen, game.index)
                text_input.helping_2 = False
            else:
                text_input.helping_2 = True
                text_input.draw(screen, game.index)
            game.draw_points(screen)

        pygame.quit()

    def draw(self, which) -> None:
        pygame.display.update()
        self.screen.blit(which[self.game.index], (0, 0))

if __name__ == '__main__':
    M = Main()
    M.run()
