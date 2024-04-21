import pygame as pg
import math
import variable_constructor as variable
import pickle

from screen_update_classes import ScreenUpdate

# ! чтобы создать новую карту:
# * 1) создаем в папке maps файл с названием карты (map_1.p)
# * 2) меняем в файле variable_constructor значение переменной name_file на имя карты
# * 3) меняем в файле variable_constructor значение переменной bg ссылку на нужный фон


class ConstructorBg:
    def __init__(self, screen, screen_update):
        self.w_cell = variable.w_cell
        self.h_cell = variable.h_cell
        self.W = variable.W
        self.H = variable.H
        self.elements = variable.elements
        self.name_file = variable.name_file
        self.bg = variable.bg
        self.link_block = variable.link_block_default
        self.color_green = variable.green
        self.screen = screen

        self.screen_update = screen_update

        self.data_file = self.screen_update.get_data()
        self.brick_coord = self.data_file[1]

    def get_coordinats(self, position):
        self.x = position[0]
        self.y = position[1]

        self.number_cell_x = math.ceil(self.x / self.w_cell)
        self.x_pos = self.w_cell * (self.number_cell_x - 1)
        self.number_cell_y = math.ceil(self.y / self.h_cell)
        self.y_pos = self.h_cell * (self.number_cell_y - 1)
        return (self.x_pos, self.y_pos)

    def save_data(self):
        self.data_full = (self.bg, self.brick_coord)
        pickle.dump(self.data_full, open(f"{self.name_file}.p", "wb"))

    def add_cell(self, position):
        self.pos = self.get_coordinats(position)

        self.square_1 = pg.image.load(self.link_block)
        self.screen.blit(self.square_1, (self.pos[0], self.pos[1]))
        pg.display.update()

        self.brick_coord[f"{self.link_block}"][f"{self.pos[0]}-{self.pos[1]}"] = {
            "x": self.pos[0],
            "y": self.pos[1],
        }

        self.save_data()

        return self.brick_coord

    def check_cell(self, position):
        self.pos = self.get_coordinats(position)

        self.x = self.pos[0]
        self.y = self.pos[1]
        self.coord = {"x": self.x, "y": self.y}
        for key, value in list(self.brick_coord[f"{self.link_block}"].items()):
            if value == self.coord:
                return self.coord

    def del_cell(self, coord):
        for key, value in list(self.brick_coord[f"{self.link_block}"].items()):
            if value == coord:
                del self.brick_coord[f"{self.link_block}"][f"{key}"]
                # выводится на экран полученным координатам
            # сохраняем список
        self.save_data()

        return self.brick_coord

    def get_link_image(self, coord):
        self.link_coord = self.get_coordinats(coord)

        for key, value in self.elements.items():
            if value == self.link_coord:
                self.link_block = key
                return key
