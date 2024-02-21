import pygame as pg
import pickle
import grid_bg
import variable
import os


elements = variable.elements
name_file = variable.name_file


def get_data():
    brick_coord = {}
    for key in elements.keys():
        brick_coord[f"{key}"] = {}

    if os.path.getsize(f"{name_file}.p") > 0:
        with open(f"{name_file}.p", "rb") as f:
            unpickler = pickle.Unpickler(f)
            # if file is not empty scores will be equal
            # to the value unpickled
            brick_coord = unpickler.load()

    return brick_coord


def screen_update(screen):
    # получаем картинку и сохраняем в переменную
    bg = pg.image.load("assets/images/bg-grass.jpg")
    screen.blit(bg, (0, 0))

    for key, value in elements.items():
        # загружаем изображение по ключу image (не меняется)
        square = pg.image.load(key)

        # выводится на экран полученным координатам
        screen.blit(square, (value[0], value[1]))

    grid_bg.handle_grid(screen)

    brick_coord = {}
    for key in elements.keys():
        brick_coord[f"{key}"] = {}

    bricks = get_data()
    # bricks = pickle.load(open(f"{name_file}.p", "rb")) or brick_coord

    # пробегаемся по списку с ключом coordinats (так как все координаты лежат именно там) и при
    # каждой итерации получаем brick:  {'x': 660, 'y': 176}
    for key in bricks.keys():
        for brick in bricks[f"{key}"].values():
            # загружаем изображение по ключу image (не меняется)
            square = pg.image.load(key)
            # выводится на экран полученным координатам
            screen.blit(square, (brick["x"], brick["y"]))
    # обновляем экран
    # pg.display.flip()
