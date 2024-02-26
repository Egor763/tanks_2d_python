import pygame as pg
import variable
import tanks_screen
from manage_tanks import manage_my_tank
import pickle


# brick_coord = pickle.load(open(f"{name_file}.p", "rb"))


pg.init()

W = variable.W
H = variable.H
link_my_tank = variable.my_tank


window_size = (W, H)

# задаем название окна
pg.display.set_caption("Танки")

# создаем окно
screen = pg.display.set_mode(window_size)

# переазагружаем страницу
# tanks_screen.screen_update(screen)
player_tank = tanks_screen.draw_elements(screen)


# обновляем экран для отображения изменений
pg.display.flip()
# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    # tanks_screen.screen_update(screen)

    tanks_screen.handle_image_screen(screen)
    for event in pg.event.get():

        # добавляем слушатель при нажатии на клетку
        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            # добавляем квадрат
            manage_my_tank.turn_my_tank(screen, 0, player_tank)
            manage_my_tank.forward_go(event.key)

        elif event.type == pg.KEYUP and event.key == pg.K_UP:
            # print("k_up up")
            manage_my_tank.forward_stop(event.key)

        elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            # добавляем квадрат
            manage_my_tank.turn_my_tank(screen, -90, player_tank)
            manage_my_tank.forward_go(event.key)

        elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
            manage_my_tank.forward_stop(event.key)

        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            # добавляем квадрат
            manage_my_tank.turn_my_tank(screen, 180, player_tank)
            manage_my_tank.forward_go(event.key)

        elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
            manage_my_tank.forward_stop(event.key)

        elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            # добавляем квадрат
            manage_my_tank.turn_my_tank(screen, 90, player_tank)
            manage_my_tank.forward_go(event.key)

        elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
            manage_my_tank.forward_stop(event.key)

        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            print("пробел")

        elif event.type == pg.QUIT:
            pg.quit()
            exit()

    manage_my_tank.move_image(player_tank)
