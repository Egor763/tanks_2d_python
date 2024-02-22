import pygame as pg
import pickle
import constructor_bg
import variable_constructor as variable
import os


elements = variable.elements
name_file = variable.name_file


# функция которая получает данные из сохраненных файлов (map_1.p)
# проверяется файл если он пустой то создается новый словарь
def get_data():
    # объявляем словарь
    brick_coord = {}
    # находим ключи в словаре elements (ссылки на изображения)
    for key in elements.keys():
        brick_coord[f"{key}"] = {}

    # проверяется пустой ли файл или нет, имя файла получаем из переменной variable (name файл)
    # если размер файла больше нуля то файл не пустой и файл загрузится
    if os.path.getsize(f"{name_file}.p") > 0:
        with open(f"{name_file}.p", "rb") as f:
            unpickler = pickle.Unpickler(f)

            brick_coord = unpickler.load()

    # возвращаем полученный список либо из файла, либо из пустого словаря
    return brick_coord


def screen_update(screen):
    # получаем картинку и сохраняем в переменную
    bg = pg.image.load("game/assets/images/backgrounds/bg-grass.jpg")
    screen.blit(bg, (0, 0))

    for key, value in elements.items():
        # загружаем изображение по ключу image (не меняется)
        square = pg.image.load(key)

        # выводится на экран полученным координатам
        screen.blit(square, (value[0], value[1]))

    constructor_bg.handle_grid(screen)

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
