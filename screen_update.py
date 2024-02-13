import pygame as pg
import pickle
import grid_bg


def screen_update(screen):
    # получаем картинку и сохраняем в переменную
    bg = pg.image.load("assets/images/bg-grass.jpg")
    screen.blit(bg, (0, 0))

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
