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
key2mvmt = variable.key2mvmt
FPS = variable.FPS
FPS_CLOCK = pg.time.Clock()


window_size = (W, H)

# задаем название окна
pg.display.set_caption("Танки")

# создаем окно
screen = pg.display.set_mode(window_size)

key = ""
# time_delay = 1000

# переазагружаем страницу
# tanks_screen.screen_update(screen)
player_tank = tanks_screen.draw_elements(screen)

end_time = pg.time.get_ticks() + 3000
# обновляем экран для отображения изменений
pg.display.flip()
# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    # tanks_screen.screen_update(screen)
    FPS_CLOCK.tick(FPS)
    current_time = pg.time.get_ticks()

    tanks_screen.handle_image_screen(screen)
    for event in pg.event.get():

        # добавляем слушатель при нажатии на клетку
        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            # добавляем квадрат
            manage_my_tank.turn_my_tank(screen, 0, player_tank)
            manage_my_tank.forward_go(event.key, player_tank)

        elif event.type == pg.KEYUP and event.key == pg.K_UP:
            key = event.key
            manage_my_tank.forward_stop(key, player_tank)
            # end_time = pg.time.get_ticks() + time_delay

        elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            # добавляем квадрат
            manage_my_tank.turn_my_tank(screen, -90, player_tank)
            manage_my_tank.forward_go(event.key, player_tank)

        elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
            key = event.key
            # end_time = pg.time.get_ticks() + time_delay
            manage_my_tank.forward_stop(key, player_tank)

        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            # добавляем квадрат
            manage_my_tank.turn_my_tank(screen, 180, player_tank)
            manage_my_tank.forward_go(event.key, player_tank)

        elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
            key = event.key
            # end_time = pg.time.get_ticks() + time_delay
            manage_my_tank.forward_stop(key, player_tank)

        elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            # добавляем квадрат
            manage_my_tank.turn_my_tank(screen, 90, player_tank)
            manage_my_tank.forward_go(event.key, player_tank)

        elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
            key = event.key
            # end_time = pg.time.get_ticks() + time_delay
            manage_my_tank.forward_stop(key, player_tank)

        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            print("пробел")

        elif event.type == pg.QUIT:
            pg.quit()
            exit()

    # if current_time > end_time:
    #     for k in key2mvmt.keys():
    #         if k == key:
    #             print("key: ", key2mvmt[key])

    #             if key2mvmt[key]:

    #                 manage_my_tank.forward_stop(key, player_tank)

    manage_my_tank.move_image(player_tank)
