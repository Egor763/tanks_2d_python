import pygame as pg
import variable
from tanks_screen_classes import TanksScreen
from manage_tanks import manage_my_tank


class Tanks:
    def __init__(self):
        pg.init()

        self.W = variable.W
        self.H = variable.H
        self.link_my_tank = variable.my_tank
        self.key2mvmt = variable.key2mvmt
        self.FPS = variable.FPS
        self.FPS_CLOCK = pg.time.Clock()

        self.tank_shot_sound = pg.mixer.Sound(
            "game/assets/sounds/Sound/tank_fire_bullet.ogg"
        )

        self.window_size = (self.W, self.H)

        pg.display.set_caption("Танки")

        self.tanks_screen_update = TanksScreen()

        self.screen = pg.display.set_mode(self.window_size)

        self.key = ""
        self.time_delay = 100

        self.player_tank = self.tanks_screen_update.draw_elements(self.screen)

        self.end_time = 0

        pg.display.flip()

        self.timer_event = pg.USEREVENT
        pg.time.set_timer(self.timer_event, 500)

        self.state_key = False
        self.key_fire = False

    def run_game(self):
        while True:
            self.FPS_CLOCK.tick(self.FPS)
            self.current_time = pg.time.get_ticks()

            self.tanks_screen_update.handle_image_screen(self.screen)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                    if not self.key == event.key:
                        print("u")
                        self.end_time = pg.time.get_ticks() + self.time_delay
                        manage_my_tank.turn_my_tank(self.screen, 0, self.player_tank)

                    manage_my_tank.forward_go(event.key, self.player_tank)

                elif event.type == pg.KEYUP and event.key == pg.K_UP:
                    self.key = event.key
                    manage_my_tank.forward_stop(self.key, self.player_tank)

                elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                    if not self.key == event.key:
                        print("r")
                        self.end_time = pg.time.get_ticks() + self.time_delay
                        manage_my_tank.turn_my_tank(self.screen, -90, self.player_tank)

                    manage_my_tank.forward_go(event.key, self.player_tank)

                elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
                    self.key = event.key
                    manage_my_tank.forward_stop(self.key, self.player_tank)

                elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                    if not self.key == event.key:
                        print("d")
                        self.end_time = pg.time.get_ticks() + self.time_delay
                        manage_my_tank.turn_my_tank(self.screen, 180, self.player_tank)

                    manage_my_tank.forward_go(event.key, self.player_tank)

                elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
                    self.key = event.key
                    manage_my_tank.forward_stop(self.key, self.player_tank)

                elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                    if not self.key == event.key:
                        print("d")
                        self.end_time = pg.time.get_ticks() + self.time_delay
                        manage_my_tank.turn_my_tank(self.screen, 90, self.player_tank)

                    manage_my_tank.forward_go(event.key, self.player_tank)

                elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
                    self.key = event.key
                    manage_my_tank.forward_stop(self.key, self.player_tank)

                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.key_fire = True
                    self.tank_shot_sound.play()

                elif event.type == pg.KEYUP and event.key == pg.K_SPACE:
                    self.key_fire = False

                elif event.type == self.timer_event and self.key_fire:
                    self.tank_shot_sound.play()

                elif event.type == pg.QUIT:
                    pg.quit()
                    exit()

            if self.current_time < self.end_time:
                self.state_key = True

            else:
                self.state_key = False

            manage_my_tank.move_image(self.player_tank, self.state_key)


if __name__ == "__main__":
    ai = Tanks()
    ai.run_game()
