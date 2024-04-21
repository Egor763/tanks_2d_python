# import pygame as pg
# import pickle
# import constructor_bg
# import variable_constructor as variable
# import os


# elements = variable.elements
# name_file = variable.name_file
# bg = variable.bg


# # функция которая получает данные из сохраненных файлов (map_1.p)
# # проверяется файл если он пустой то создается новый словарь
# def get_data():
#     # объявляем словарь
#     brick_coord = {}
#     # находим ключи в словаре elements (ссылки на изображения)
#     for key in elements.keys():
#         brick_coord[f"{key}"] = {}

#     # в переменную дата кладем котреж python состоящий из двух элеметов, 1 - фон (variable_constructor), 2 - словарь с координатами
#     data_file = (bg, brick_coord)

#     # проверяется пустой ли файл или нет, имя файла получаем из переменной variable (name файл)
#     # если размер файла больше нуля то файл не пустой и файл загрузится
#     if os.path.getsize(f"{name_file}.p") > 0:
#         with open(f"{name_file}.p", "rb") as f:
#             unpickler = pickle.Unpickler(f)

#             data_file = unpickler.load()

#     # возвращаем полученный список либо из файла, либо из пустого словаря
#     return data_file


# # устанавливаем образцы блоков
# def set_templates(screen):
#     # перебираем ключи и значения в списке elements
#     for key, value in elements.items():
#         # загружаем изображение по ключу (ссылки на изображение)
#         square = pg.image.load(key)

#         # выводится на экран полученным координатам
#         screen.blit(square, (value[0], value[1]))


# # функция обновления экрана
# def screen_update(screen):
#     # получаем кортеж с данными
#     data_file = get_data()

#     # получаем код из кортеджа по индексу 0
#     bg = pg.image.load(data_file[0])
#     screen.blit(bg, (0, 0))

#     # устанавливаем образцы
#     set_templates(screen)

#     # рисуем вертикальную и горизонтальную линии
#     constructor_bg.handle_grid(screen)

#     # получаем координаты из кортежа по индексу 1
#     bricks = data_file[1]

#     # 1. в словаре bricks получаем ключи
#     # 2. в словаре bricks по полученному ключу получаем значения
#     for key in bricks.keys():
#         for brick in bricks[f"{key}"].values():
#             # загружаем изображение по ключу
#             square = pg.image.load(key)
#             # выводится на экран полученным координатам
#             screen.blit(square, (brick["x"], brick["y"]))
