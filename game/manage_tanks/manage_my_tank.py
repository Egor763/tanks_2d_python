import pygame as pg
import tanks_screen
import variable
from pygame.locals import *
import math


key2mvmt = variable.key2mvmt
link_my_tank = variable.my_tank
w_tank = variable.w_cell
h_tank = variable.h_cell
tank_x = 100
tank_y = 100
tank_move = 1
movement = 3
IMAGE = pg.image.load(link_my_tank)
coord_tank = 0
LEFT = "left"
deg_tanks = 0
W = variable.W
H = variable.H
w_cell = variable.w_cell
h_cell = variable.h_cell
number_cell = 0


def turn_my_tank(screen, angle, player_tank):
    # для поворота получаем первоначальное изображение по захорткоженной ссылке
    image_tank = pg.image.load(link_my_tank)
    # поварачиваем изображение на нужный угол
    rotated_image = pg.transform.rotate(image_tank, angle)
    # повернутое изображение сохраняем в словаре player_tank
    player_tank["surface"] = rotated_image

    # получаем текущие координаты из словаря player_tank по ключу rect
    rect = player_tank["rect"]
    # координаты отцентрованного изображения
    new_rect = (
        rotated_image.get_rect(
            center=image_tank.get_rect(topleft=(rect.x, rect.y)).center
        ).topleft,
    )

    screen.blit(rotated_image, new_rect)

    return rotated_image, new_rect


def forward_go(key, player_tank):
    if key in key2mvmt:
        key2mvmt[key] = True


def forward_stop(key, player_tank):

    # global coord_tank
    # y = player_tank["rect"].y
    # number_cell = math.ceil(y / h_cell)
    # coord_tank = number_cell * h_cell

    if key in key2mvmt:
        key2mvmt[key] = False


def move_image(player_tank):
    for k in key2mvmt.keys():
        if key2mvmt[k]:
            move_rect(player_tank["rect"], k, movement)
        # else:

        # print("stopped")

    pg.display.update()


def move_rect(rect, key, distance):
    if key == K_UP:
        rect.y -= distance
    elif key == K_DOWN:
        rect.y += distance
    elif key == K_LEFT:
        rect.x -= distance
    elif key == K_RIGHT:
        rect.x += distance


# движение танка относительно сетки
# def handle_move_my_tank():
