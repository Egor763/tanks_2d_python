import pygame as pg
import pickle
import variable

color_green = variable.green
w_cell = variable.w_cell
h_cell = variable.h_cell
W = variable.W
H = variable.H


# функция которая получает данные из сохраненных файлов (map_1.p)
# проверяется файл если он пустой то создается новый словарь
def get_data():
    data_file = pickle.load(open("maps/map_1.p", "rb"))
    return data_file


# возвращаем полученный список либо из файла, либо из пустого словаря


# функция обновления экрана
def screen_update(screen):
    # получаем кортеж с данными
    data_file = get_data()

    # получаем код из кортеджа по индексу 0
    bg = pg.image.load(data_file[0])
    screen.blit(bg, (0, 0))

    # рисуем вертикальную и горизонтальную линии
    handle_grid(screen)

    # получаем координаты из кортежа по индексу 1
    bricks = data_file[1]

    # 1. в словаре bricks получаем ключи
    # 2. в словаре bricks по полученному ключу получаем значения
    for key in bricks.keys():
        for brick in bricks[f"{key}"].values():
            # загружаем изображение по ключу
            square = pg.image.load(key)
            # выводится на экран полученным координатам
            screen.blit(square, (brick["x"], brick["y"]))


def handle_grid(screen):
    # определяем координаты верхней левой точки экрана
    y = 1
    x = 1

    # по оси y
    while y < H:
        pg.draw.line(screen, color_green, (0, y), (W, y), 1)
        y = y + h_cell

    # по оси x
    while x < W:
        pg.draw.line(screen, color_green, (x, 0), (x, H), 1)
        x = x + w_cell
