import math
import pygame as pg
import variable_constructor as variable
import pickle
import screen_update as screen_update


w_cell = variable.w_cell
h_cell = variable.h_cell
W = variable.W
H = variable.H
elements = variable.elements
name_file = variable.name_file


brick_coord = screen_update.get_data()
# загружаем сохраненные файлы, кладем в переменную bricks
bricks = {}
for key in elements.keys():
    bricks[f"{key}"] = {}

# brick_coord = pickle.load(open(f"{name_file}.p", "rb")) or bricks

my_surface = pg.Surface((w_cell, h_cell))
my_surface.fill((0, 0, 0, 0))

link_block = "game/assets/images/blocks/bricks_block.png"


def handle_grid(screen):
    # горизонтальная линия
    y = 1
    x = 1

    while y < H:
        pg.draw.line(screen, variable.green, (0, y), (W, y), 1)
        y = y + h_cell

    while x < W:
        pg.draw.line(screen, variable.green, (x, 0), (x, H), 1)
        x = x + w_cell


def get_coordinats(position):
    x = position[0]
    y = position[1]

    number_cell_x = math.ceil(x / w_cell)
    x_pos = w_cell * (number_cell_x - 1)
    number_cell_y = math.ceil(y / h_cell)
    y_pos = h_cell * (number_cell_y - 1)
    return (x_pos, y_pos)


def add_cell(position, screen):
    pos = get_coordinats(position)

    square_1 = pg.image.load(link_block)
    screen.blit(square_1, (pos[0], pos[1]))
    pg.display.update()

    brick_coord[f"{link_block}"][f"{pos[0]}-{pos[1]}"] = {
        "x": pos[0],
        "y": pos[1],
    }

    # сохраняем список
    pickle.dump(brick_coord, open(f"{name_file}.p", "wb"))
    return brick_coord


def check_cell(position):
    pos = get_coordinats(position)

    x = pos[0]
    y = pos[1]
    coord = {"x": x, "y": y}
    for key, value in list(brick_coord[f"{link_block}"].items()):
        if value == coord:
            return coord


def del_cell(coord):

    for key, value in list(brick_coord[f"{link_block}"].items()):
        if value == coord:
            del brick_coord[f"{link_block}"][f"{key}"]
            # выводится на экран полученным координатам
        # сохраняем список
    pickle.dump(brick_coord, open(f"{name_file}.p", "wb"))
    return brick_coord


def get_link_image(coord):
    global link_block
    link_coord = get_coordinats(coord)
    for key, value in elements.items():
        if value == link_coord:
            link_block = key
            return key
