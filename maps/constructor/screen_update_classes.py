import pygame as pg
import pickle

# import constructor_bg
# from constructor_bg_classes import ConstructorBg
import variable_constructor as variable
import os


class ScreenUpdate:
    def __init__(self, screen):
        self.w_cell = variable.w_cell
        self.h_cell = variable.h_cell
        self.elements = variable.elements
        self.name_file = variable.name_file
        self.bg = variable.bg
        self.screen = screen
        self.W = variable.W
        self.H = variable.H
        self.color_green = variable.green

        # self.screen = screen

        # self.constructor_bg = ConstructorBg()

    def handle_grid(self):
        self.y = 1
        self.x = 1

        # по оси y
        while self.y < self.H:
            pg.draw.line(
                self.screen, self.color_green, (0, self.y), (self.W, self.y), 1
            )

            self.y = self.y + self.h_cell

        # по оси x
        while self.x < self.W:
            pg.draw.line(
                self.screen, self.color_green, (self.x, 0), (self.x, self.H), 1
            )
            self.x = self.x + self.w_cell

    def get_data(self):
        self.brick_coord = {}
        for key in self.elements.keys():
            self.brick_coord[f"{key}"] = {}

        self.data_file = (self.bg, self.brick_coord)

        if os.path.getsize(f"{self.name_file}.p") > 0:
            with open(f"{self.name_file}.p", "rb") as f:
                self.unpicker = pickle.Unpickler(f)

                self.data_file = self.unpicker.load()

        return self.data_file

    def set_templates(self):
        for key, value in self.elements.items():
            self.square = pg.image.load(key)

            self.screen.blit(self.square, (value[0], value[1]))

    def screen_update(self):
        # получаем кортеж с данными
        self.data_file = self.get_data()

        # получаем код из кортеджа по индексу 0
        self.bg = pg.image.load(self.data_file[0])
        self.screen.blit(self.bg, (0, 0))

        # устанавливаем образцы
        self.set_templates()

        self.handle_grid()

        self.bricks = self.data_file[1]

        # 1. в словаре bricks получаем ключи
        # 2. в словаре bricks по полученному ключу получаем значения
        for key in self.bricks.keys():
            for brick in self.bricks[f"{key}"].values():
                # загружаем изображение по ключу
                square = pg.image.load(key)
                # выводится на экран полученным координатам
                self.screen.blit(square, (brick["x"], brick["y"]))
