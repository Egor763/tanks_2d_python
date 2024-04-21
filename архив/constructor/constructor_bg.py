# import math
# import pygame as pg
# import variable_constructor as variable
# import pickle

# # import screen_update as screen_update
# from screen_update_classes import ScreenUpdate

# # ! чтобы создать новую карту:
# # * 1) создаем в папке maps файл с названием карты (map_1.p)
# # * 2) меняем в файле variable_constructor значение переменной name_file на имя карты
# # * 3) меняем в файле variable_constructor значение переменной bg ссылку на нужный фон


# # добалвляем новые переменные
# w_cell = variable.w_cell
# h_cell = variable.h_cell
# W = variable.W
# H = variable.H
# elements = variable.elements
# name_file = variable.name_file
# bg = variable.bg
# # определяем ссылку на блок и присваиваем значение по умолчанию (кирпичный)
# link_block = variable.link_block_default
# color_green = variable.green

# screen_update = ScreenUpdate()

# # вызываем функцию get_data
# data_file = screen_update.get_data()
# # извлекаем из кортежа кирпичи по индексу 1
# brick_coord = data_file[1]


# # сетка на экране
# def handle_grid(screen):
#     # определяем координаты верхней левой точки экрана
#     y = 1
#     x = 1

#     # по оси y
#     while y < H:
#         pg.draw.line(screen, color_green, (0, y), (W, y), 1)
#         y = y + h_cell

#     # по оси x
#     while x < W:
#         pg.draw.line(screen, color_green, (x, 0), (x, H), 1)
#         x = x + w_cell


# # координаты начала клетки
# def get_coordinats(position):
#     x = position[0]
#     y = position[1]

#     number_cell_x = math.ceil(x / w_cell)
#     x_pos = w_cell * (number_cell_x - 1)
#     number_cell_y = math.ceil(y / h_cell)
#     y_pos = h_cell * (number_cell_y - 1)
#     return (x_pos, y_pos)


# def save_data(data):
#     data_full = (bg, data)
#     pickle.dump(data_full, open(f"{name_file}.p", "wb"))


# def add_cell(position, screen):
#     pos = get_coordinats(position)

#     square_1 = pg.image.load(link_block)
#     screen.blit(square_1, (pos[0], pos[1]))
#     pg.display.update()

#     brick_coord[f"{link_block}"][f"{pos[0]}-{pos[1]}"] = {
#         "x": pos[0],
#         "y": pos[1],
#     }

#     # сохраняем список
#     save_data(brick_coord)

#     # pickle.dump(brick_coord, open(f"{name_file}.p", "wb"))
#     return brick_coord


# def check_cell(position):
#     pos = get_coordinats(position)

#     x = pos[0]
#     y = pos[1]
#     coord = {"x": x, "y": y}
#     for key, value in list(brick_coord[f"{link_block}"].items()):
#         if value == coord:
#             return coord


# def del_cell(coord):

#     for key, value in list(brick_coord[f"{link_block}"].items()):
#         if value == coord:
#             del brick_coord[f"{link_block}"][f"{key}"]
#             # выводится на экран полученным координатам
#         # сохраняем список
#     save_data(brick_coord)
#     return brick_coord


# # выбираем нужную ссылку
# def get_link_image(coord):
#     # global - делает видимой глобальную переменную внутри функции и можно перезаписывать значения
#     global link_block
#     link_coord = get_coordinats(coord)
#     # пробегаемся по словарю с переменной elements с ссылками на блоки и при выполнении условии присваиваем глобальной переменнойS
#     # выбранное значение
#     for key, value in elements.items():
#         if value == link_coord:
#             link_block = key
#             return key


# # ! строение словаря с координатами
# # brick_coord[f"{link_block}"][f"{pos[0]}-{pos[1]}"] = {
# #     "x": pos[0],
# #     "y": pos[1],
# # }


# # словарь
# # "link_1" - ссылка на кубик "ключ словаря"
# # "x-y" - ключ вложенного словаря по ключу link_1 (первый вложенный словарь)
# # "x" - ключ вложенного словаря по ключу "x-y" (словарь вложенный в словарь)
# # brick_coord = {
# #     "link_1": {
# #         "x-y": {
# #             "x": x,
# #             "y": y,
# #         }
# #     },
# #     "link_2": {
# #         "x-y": {
# #             "x": x,
# #             "y": y,
# #         }
# #     },
# #     "link_3": {
# #         "x-y": {
# #             "x": x,
# #             "y": y,
# #         }
# #     },
# # }
