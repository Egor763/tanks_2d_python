import pygame

# import constructor_bg
from constructor_bg_classes import ConstructorBg
import variable_constructor as variable
from screen_update_classes import ScreenUpdate


class Constructor:
    def __init__(self):
        pygame.init()
        self.W = variable.W
        self.H = variable.H
        self.window_size = (self.W, self.H)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Конструктор")

        self.screen_update = ScreenUpdate(self.screen)

        self.screen_update.screen_update()

        self.constructor_bg = ConstructorBg(self.screen, self.screen_update)

        pygame.display.flip()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # добавляем квадрат
                    if event.pos[0] < 880:
                        coord = self.constructor_bg.check_cell(event.pos)
                        # вызываем функцию и возвращаем значения и кладем в переменную bricks
                        if not coord:
                            self.bricks = self.constructor_bg.add_cell(event.pos)
                        # удаляем квадрат
                        else:
                            self.bricks = self.constructor_bg.del_cell(coord)

                            self.screen_update.screen_update()
                            pygame.display.update()
                    # получаем ссылку на изображение при щелчке на квадрат
                    else:
                        self.constructor_bg.get_link_image(event.pos)

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    exit()


if __name__ == "__main__":
    ai = Constructor()
    ai.run_game()
