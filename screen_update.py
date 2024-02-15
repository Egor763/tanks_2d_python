import pygame as pg
import pickle
import grid_bg


def screen_update(screen):
    # получаем картинку и сохраняем в переменную
    bg = pg.image.load("assets/images/bg-grass.jpg")
    screen.blit(bg, (0, 0))

    elements = {
        "headquarters": "assets/images/headquarters.png",
        "bricks": "assets/images/bricks_block.png",
        "concrete": "assets/images/concrete_block.png",
        "bricks_block_left": "assets/images/bricks_block_left.png",
        "bricks_block_right": "assets/images/bricks_block_right.png",
    }

    coord = 660

    for element in elements.values():
        # загружаем изображение по ключу image (не меняется)
        square = pg.image.load(element)

        # выводится на экран полученным координатам
        screen.blit(square, (880, coord))
        coord = coord - 88

    # headquarters = pg.image.load("assets/images/headquarters.png")
    # screen.blit(headquarters, (880, 660))

    # bricks_block = pg.image.load("assets/images/bricks_block.png")
    # screen.blit(bricks_block, (880, 570))

    # concrete_block = pg.image.load("assets/images/concrete_block.png")
    # screen.blit(concrete_block, (880, 482))

    grid_bg.handle_grid(screen)

    bricks = pickle.load(open("save.p", "rb"))
    print("bricks: ", bricks)

    # пробегаемся по списку с ключом coordinats (так как все координаты лежат именно там) и при
    # каждой итерации получаем brick:  {'x': 660, 'y': 176}
    for brick in bricks["coordinates"].values():
        # загружаем изображение по ключу image (не меняется)
        square = pg.image.load(bricks["image"])
        # выводится на экран полученным координатам
        screen.blit(square, (brick["x"], brick["y"]))
    # обновляем экран
    pg.display.flip()
