# import pygame as pg
# import variable
# import tanks_screen
# from manage_tanks import manage_my_tank
# import pickle
# from tanks_screen_classes import TanksScreen


# # brick_coord = pickle.load(open(f"{name_file}.p", "rb"))


# pg.init()

# W = variable.W
# H = variable.H
# link_my_tank = variable.my_tank
# key2mvmt = variable.key2mvmt
# FPS = variable.FPS
# FPS_CLOCK = pg.time.Clock()

# # подключение звука
# tank_shot_sound = pg.mixer.Sound("game/assets/sounds/Sound/tank_fire_bullet.ogg")


# window_size = (W, H)

# # задаем название окна
# pg.display.set_caption("Танки")

# tanks_screen_update = TanksScreen()

# # создаем окно
# screen = pg.display.set_mode(window_size)

# key = ""
# time_delay = 100

# # переазагружаем страницу
# # tanks_screen_update.screen_update(screen)
# player_tank = tanks_screen_update.draw_elements(screen)

# end_time = 0
# # обновляем экран для отображения изменений
# pg.display.flip()
# # показываем окно, пока пользователь не нажмет кнопку "Закрыть"

# timer_event = pg.USEREVENT
# pg.time.set_timer(timer_event, 500)

# state_key = False

# # ключ кнопки пробел
# key_fire = False


# while True:
#     # tanks_screen_update.screen_update(screen)
#     FPS_CLOCK.tick(FPS)
#     current_time = pg.time.get_ticks()

#     tanks_screen_update.handle_image_screen(screen)
#     for event in pg.event.get():

#         # добавляем слушатель при нажатии на клетку
#         if event.type == pg.KEYDOWN and event.key == pg.K_UP:
#             # добавляем квадрат
#             if not key == event.key:
#                 print("u")
#                 end_time = pg.time.get_ticks() + time_delay
#                 manage_my_tank.turn_my_tank(screen, 0, player_tank)

#             manage_my_tank.forward_go(event.key, player_tank)

#         elif event.type == pg.KEYUP and event.key == pg.K_UP:
#             key = event.key
#             manage_my_tank.forward_stop(key, player_tank)

#         elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
#             # добавляем квадрат
#             if not key == event.key:
#                 print("r")
#                 end_time = pg.time.get_ticks() + time_delay
#                 manage_my_tank.turn_my_tank(screen, -90, player_tank)

#             manage_my_tank.forward_go(event.key, player_tank)

#         elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
#             key = event.key
#             # end_time = pg.time.get_ticks() + time_delay
#             manage_my_tank.forward_stop(key, player_tank)

#         elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
#             # добавляем квадрат
#             if not key == event.key:
#                 print("d")

#                 end_time = pg.time.get_ticks() + time_delay
#                 manage_my_tank.turn_my_tank(screen, 180, player_tank)

#             manage_my_tank.forward_go(event.key, player_tank)

#         elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
#             key = event.key
#             # end_time = pg.time.get_ticks() + time_delay
#             manage_my_tank.forward_stop(key, player_tank)

#         elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
#             # добавляем квадрат
#             if not key == event.key:
#                 print("l")
#                 end_time = pg.time.get_ticks() + time_delay
#                 manage_my_tank.turn_my_tank(screen, 90, player_tank)

#             manage_my_tank.forward_go(event.key, player_tank)

#         elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
#             key = event.key
#             manage_my_tank.forward_stop(key, player_tank)
#         # ==== ПРОБЕЛ ===========================================
#         elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
#             key_fire = True
#             tank_shot_sound.play()

#         elif event.type == pg.KEYUP and event.key == pg.K_SPACE:
#             key_fire = False
#         # звуки выстрела
#         elif event.type == timer_event and key_fire:
#             # проигрыватель звука
#             tank_shot_sound.play()
#         # ==================================================
#         elif event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     if current_time < end_time:
#         state_key = True
#     else:
#         state_key = False

#     manage_my_tank.move_image(player_tank, state_key)
