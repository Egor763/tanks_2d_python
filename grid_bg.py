import math
import pygame as pg
import variable
import pickle
import screen_update


w_cell = variable.w_cell
h_cell = variable.h_cell
W = variable.W
H = variable.H


# загружаем сохраненные файлы, кладем в переменную bricks
brick_coord = pickle.load(open("save.p", "rb"))

my_surface = pg.Surface((w_cell, h_cell))
my_surface.fill((0, 0, 0, 0))

# brick_coord = {"image": "assets/images/bricks_block.png", "coordinates": {}}


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


def get_cell(position, screen):
    pos = get_coordinats(position)
    print("pos: ", pos)

    square_1 = pg.image.load("assets/images/bricks_block.png")
    screen.blit(square_1, (pos[0], pos[1]))
    pg.display.update()

    # brick_coord["coordinates"].append({"x": pos[0], "y": pos[1]})
    brick_coord["coordinates"][f"{pos[0]}-{pos[1]}"] = {
        "x": pos[0],
        "y": pos[1],
    }

    # сохраняем список
    pickle.dump(brick_coord, open("save.p", "wb"))
    return brick_coord


def check_cell(position):
    pos = get_coordinats(position)

    x = pos[0]
    y = pos[1]
    coord = {"x": x, "y": y}
    # print("coord: ", coord)

    for brick in brick_coord["coordinates"].values():
        if brick == coord:
            # print(brick)
            return coord
        # print(brick)
    # print(y)


def del_cell(coord, screen):

    for key, value in list(brick_coord["coordinates"].items()):
        if brick_coord["coordinates"][key] == coord:
            print("brick: ", key)
            del brick_coord["coordinates"][key]
            # выводится на экран полученным координатам
        # сохраняем список
    pickle.dump(brick_coord, open("save.p", "wb"))
    return brick_coord


# square_1 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_1, (88, 44))

# square_2 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_2, (132, 44))

# square_3 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_3, (44, 88))

# square_4 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_4, (88, 88))

# square_5 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_5, (132, 88))

# square_6 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_6, (44, 176))

# square_7 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_7, (88, 176))

# square_8 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_8, (132, 176))

# square_9 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_9, (44, 220))

# square_10 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_10, (88, 220))

# square_11 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_11, (132, 220))

# square_12 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_12, (44, 308))

# square_13 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_13, (88, 308))

# square_14 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_14, (132, 308))

# square_15 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_15, (44, 352))

# square_16 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_16, (88, 352))

# square_17 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_17, (132, 352))

# square_18 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_18, (44, 396))

# square_19 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_19, (88, 396))

# square_20 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_20, (132, 396))
