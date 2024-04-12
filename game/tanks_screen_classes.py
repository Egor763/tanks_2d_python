import pygame as pg
import pickle
import variable


class TanksScreen:
    def __init__(self):
        self.color_green = variable.green
        self.w_cell = variable.w_cell
        self.h_cell = variable.h_cell
        self.W = variable.W
        self.H = variable.H
        self.link_my_tank = variable.my_tank
        self.w_tank = variable.w_cell
        self.h_tank = variable.h_cell
        self.LEFT = variable.LEFT
        self.player_tank = variable.player_tank

    def get_data(self):
        self.data_file = pickle.load(open("maps/map_1.p", "rb"))
        return self.data_file

    def draw_elements(self, screen):
        # global self.player_tank
        self.data_file = self.get_data()
        self.bg = pg.image.load(self.data_file[0])
        screen.blit(self.bg, (0, 0))

        self.handle_grid(screen)
        self.bricks = self.data_file[1]

        for key, value in self.bricks.items():
            if key == self.link_my_tank:
                self.image_tank = pg.image.load(key)
                for key, value in value.items():
                    self.player_tank = {
                        "surface": pg.transform.scale(
                            self.image_tank, (self.w_tank, self.h_tank)
                        ),
                        "facing": self.LEFT,
                        "size": self.w_tank,
                        "x": value["x"],
                        "y": value["y"],
                    }

                    self.player_tank["rect"] = pg.Rect(
                        (
                            self.player_tank["x"],
                            self.player_tank["y"],
                            self.player_tank["size"],
                            self.player_tank["size"],
                        )
                    )

        return self.player_tank

    def handle_image_screen(self, screen):
        self.data_file = self.get_data()

        self.bg = pg.image.load(self.data_file[0])
        self.bricks = self.data_file[1]
        screen.blit(self.bg, (0, 0))

        for key in self.bricks.keys():
            if not key == self.link_my_tank:
                for brick in self.bricks[f"{key}"].values():
                    self.square = pg.image.load(key)
                    screen.blit(self.square, (brick["x"], brick["y"]))

        self.handle_grid(screen)

        screen.blit(self.player_tank["surface"], self.player_tank["rect"])

    def handle_grid(self, screen):
        y = 1
        x = 1

        while y < self.H:
            pg.draw.line(screen, self.color_green, (0, y), (self.W, y), 1)
            y = y + self.h_cell

        while x < self.W:
            pg.draw.line(screen, self.color_green, (x, 0), (x, self.H), 1)
            x = x + self.w_cell
