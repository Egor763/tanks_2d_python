import pygame
import constructor_bg
import variable_constructor as variable
import screen_update as screen_update

# ! чтобы создать новую карту:
# * 1) создаем в папке maps файл с названием карты (map_1.p)
# * 2) меняем в файле variable_constructor значение переменной name_file на имя карты
# * 3) меняем в файле variable_constructor значение переменной bg ссылку на нужный фон

pygame.init()

W = variable.W
H = variable.H


window_size = (W, H)

# задаем название окна
pygame.display.set_caption("Конструктор")

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
                coord = constructor_bg.check_cell(event.pos)
                # вызываем функцию и возвращаем значения и кладем в переменную bricks
                if not coord:
                    bricks = constructor_bg.add_cell(event.pos, screen)
                # удаляем квадрат
                else:
                    bricks = constructor_bg.del_cell(coord)

                    screen_update.screen_update(screen)
                    pygame.display.update()
            # получаем ссылку на изображение при щелчке на квадрат
            else:
                constructor_bg.get_link_image(event.pos)

        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()
