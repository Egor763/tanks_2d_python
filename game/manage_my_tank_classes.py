import pygame as pg
from tanks_screen_classes import TanksScreen
import variable
from pygame.locals import *
import math
import time


class ManageMyTank:
    def __init__(self, player_tank, screen):
        pg.mixer.init()
        self.key2mvmt = variable.key2mvmt
        self.link_my_tank = variable.my_tank
        self.w_tank = variable.w_cell
        self.h_tank = variable.h_cell
        self.tank_x = variable.tank_x
        self.tank_y = variable.tank_y
        self.tank_move = variable.tank_move
        self.movement = variable.movement
        self.IMAGE = pg.image.load(self.link_my_tank)
        self.coord_tank = variable.coord_tank
        self.LEFT = "left"
        self.deg_tanks = variable.deg_tanks
        self.W = variable.W
        self.H = variable.H
        self.w_cell = variable.w_cell
        self.h_cell = variable.h_cell
        self.number_cell = variable.number_cell
        self.key_move = variable.key_move
        self.key_turn = variable.key_turn
        self.tank_sound = pg.mixer.Sound("game/assets/sounds/Sound/tankengine.ogg")
        self.player_tank = player_tank
        self.screen = screen
        self.screen_update = TanksScreen()
        self.data_file = self.screen_update.get_data()

    def turn_my_tank(self, angle):
        self.image_tank = pg.image.load(self.link_my_tank)
        self.rotated_image = pg.transform.rotate(self.image_tank, angle)
        self.player_tank["surface"] = self.rotated_image

        self.rect = self.player_tank["rect"]

        self.new_rect = self.rotated_image.get_rect(
            center=self.image_tank.get_rect(topleft=(self.rect.x, self.rect.y)).center
        ).topleft

        self.screen.blit(self.rotated_image, self.new_rect)

        pg.display.update()

        return self.rotated_image, self.new_rect

    def forward_go(self, key):
        self.key_turn = False
        if key in self.key2mvmt:
            if self.check_obstacle_start(key):
                self.key2mvmt[key] = True
                self.tank_sound.play()

            # if self.check_bricks_start(key):
            #     self.key2mvmt[key] = False
            #     self.tank_sound.stop()

    def forward_stop(self, key):
        self.tank_sound.stop()
        self.key_turn = True
        self.y = self.player_tank["rect"].y
        self.x = self.player_tank["rect"].x

        if key == K_UP:
            self.key_move = True
            self.number_cell = math.ceil(self.y / self.h_cell)
            self.coord_tank = (self.number_cell - 1) * self.h_cell
        elif key == K_DOWN:
            self.key_move = True
            self.number_cell = math.ceil(self.y / self.h_cell)
            self.coord_tank = self.number_cell * self.h_cell
        elif key == K_LEFT:
            self.key_move = False
            self.number_cell = math.ceil(self.x / self.w_cell)
            self.coord_tank = (self.number_cell - 1) * self.w_cell
        elif key == K_RIGHT:
            self.key_move = False
            self.number_cell = math.ceil(self.x / self.w_cell)
            self.coord_tank = self.number_cell * self.w_cell

    def move_image(self, state_key):
        for k in self.key2mvmt.keys():

            if self.key2mvmt[k]:
                if self.key_move:
                    self.rect_tank = self.player_tank["rect"].y
                else:
                    self.rect_tank = self.player_tank["rect"].x
                # Проверка границы клетки
                if (
                    self.coord_tank - self.movement < self.rect_tank
                    and self.coord_tank + self.movement > self.rect_tank
                    and self.key_turn
                ):
                    self.key2mvmt[k] = False

                if not state_key:
                    self.move_rect(self.player_tank["rect"], k, self.movement)
                else:
                    if self.key_turn:
                        self.key2mvmt[k] = False

        pg.display.update()

    def move_rect(self, rect, key, distance):
        if key == K_UP:
            rect.y -= distance
        if self.check_obstacle_move(key):
            self.key2mvmt[key] = False

        if self.check_bricks(key):
            self.key2mvmt[key] = False

        if key == K_DOWN:
            rect.y += distance
        if self.check_obstacle_move(key):
            self.key2mvmt[key] = False

        # if self.check_bricks(key):
        #     self.key2mvmt[key] = False

        if key == K_LEFT:
            rect.x -= distance
        if self.check_obstacle_move(key):
            self.key2mvmt[key] = False

        if key == K_RIGHT:
            rect.x += distance
        if self.check_obstacle_move(key):
            self.key2mvmt[key] = False

    def check_obstacle_move(self, button):
        if button == K_UP and self.player_tank["rect"].y < 4:
            return True
        if button == K_DOWN and self.player_tank["rect"].y > self.H - 44:
            return True
        if button == K_LEFT and self.player_tank["rect"].x < 4:
            return True
        if button == K_RIGHT and self.player_tank["rect"].x > self.W - 44:
            return True
        else:
            return False

    def check_obstacle_start(self, button):
        if button == K_UP and self.player_tank["rect"].y > 4:
            return True

        if button == K_DOWN and self.player_tank["rect"].y < self.H - 42:
            return True
        if button == K_LEFT and self.player_tank["rect"].x > 4:
            return True
        if button == K_RIGHT and self.player_tank["rect"].x < self.W - 44:
            return True
        else:
            return False

    def check_bricks(self, button):
        self.bricks = self.data_file[1]

        for key in self.bricks.keys():
            for brick in self.bricks[f"{key}"].values():
                if button == K_DOWN and self.player_tank["rect"].x > brick["x"] - 44:
                    return True

                # if button == K_LEFT and self.player_tank["rect"].y < brick["x"] - 44:
                #     print("yes")
                #     return True

                # if button == K_DOWN and self.player_tank["rect"].x > brick["x"] - 44:
                #     print("yes")
                #     return True

                else:
                    return False

    def check_bricks_start(self, button):
        self.bricks = self.data_file[1]

        for key in self.bricks.keys():
            for brick in self.bricks[f"{key}"].values():
                if button == K_DOWN and self.player_tank["rect"].x < brick["x"] - 44:
                    return True

                else:
                    return False
