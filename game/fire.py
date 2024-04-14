import pygame
import variable
from pygame.sprite import Sprite


class Fire(Sprite):
    def __init__(self, screen, player_tank):
        super().__init__()
        self.screen = screen
        self.fire = pygame.image.load("game/assets/images/move_elements/fire.png")
        self.rect = pygame.Rect(0, 0, variable.fire_width, variable.fire_height)
        self.player_tank = player_tank
        self.fire_speed = 3
        self.fire_width = variable.fire_width
        self.fire_height = variable.fire_height
        self.w_cell = variable.w_cell
        self.h_cell = variable.h_cell
        self.fire_y = self.player_tank["rect"][1] - self.fire_height

        self.y = self.rect.y

    def update(self):
        self.fire_y -= self.fire_speed

    def draw_fire(self):
        self.screen.blit(
            self.fire,
            (
                self.player_tank["rect"][0] + (self.w_cell / 2) - self.fire_width / 2,
                self.fire_y,
            ),
        )
