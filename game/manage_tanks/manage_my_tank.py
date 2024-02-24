import pygame as pg
import tanks_screen
import variable

link_my_tank = variable.my_tank

coord_tank = 0


def turn_my_tank(screen, angle):
    global coord_tank
    data = tanks_screen.get_data()
    coord_tank_dict = data[1][link_my_tank]
    # для поворота получаем изображение полностью (image_tank)
    image_tank = pg.image.load(link_my_tank)
    for value in coord_tank_dict.values():
        coord_tank = value

    # повернутое изображение
    rotated_image = pg.transform.rotate(image_tank, angle)
    # координаты отцентрованного изображения
    new_rect = (
        rotated_image.get_rect(
            center=image_tank.get_rect(
                topleft=(coord_tank["x"], coord_tank["y"])
            ).center
        ).topleft,
    )

    screen.blit(rotated_image, new_rect)
    pg.display.update()

    return rotated_image, new_rect
