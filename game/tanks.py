import pygame
import grid_bg
import game.variable as variable
import screen_update


pygame.init()

W = variable.W
H = variable.H


window_size = (W, H)

# задаем название окна
pygame.display.set_caption("Танки")

# создаем окно
screen = pygame.display.set_mode(window_size)

# переазагружаем страницу
screen_update.screen_update(screen)


# обновляем экран для отображения изменений
pygame.display.flip()
# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    for event in pygame.event.get():
        # добавляем слушатель при нажатии на клетку
        if event.type == pygame.MOUSEBUTTONDOWN:
            # добавляем квадрат
            if event.pos[0] < 880:
                coord = grid_bg.check_cell(event.pos)
                # вызываем функцию и возвращаем значения и кладем в переменную bricks
                if not coord:
                    bricks = grid_bg.add_cell(event.pos, screen)
                # удаляем квадрат
                else:
                    bricks = grid_bg.del_cell(coord)

                    screen_update.screen_update(screen)
                    pygame.display.update()
            # получаем ссылку на изображение при щелчке на квадрат
            else:
                grid_bg.get_link_image(event.pos)

        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()
