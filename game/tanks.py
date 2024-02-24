import pygame as pg
import variable
import tanks_screen
from manage_tanks import manage_my_tank

# brick_coord = pickle.load(open(f"{name_file}.p", "rb"))


pg.init()

W = variable.W
H = variable.H


window_size = (W, H)

# задаем название окна
pg.display.set_caption("Танки")

# создаем окно
screen = pg.display.set_mode(window_size)

# переазагружаем страницу
tanks_screen.screen_update(screen)


# обновляем экран для отображения изменений
pg.display.flip()
# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    for event in pg.event.get():
        # добавляем слушатель при нажатии на клетку
        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            # добавляем квадрат
            print("k_up")
            manage_my_tank.turn_my_tank(screen, 0)

        elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            # добавляем квадрат
            print("k_right")
            manage_my_tank.turn_my_tank(screen, -90)

        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            # добавляем квадрат
            print("k_down")
            manage_my_tank.turn_my_tank(screen, 180)

        elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            # добавляем квадрат
            print("k_left")
            manage_my_tank.turn_my_tank(screen, 90)

        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            print("пробел")

        elif event.type == pg.QUIT:
            pg.quit()
            exit()
