import pygame as pg
import variable

from tanks_screen_classes import TanksScreen

# from manage_tanks import self.my_tank

from manage_my_tank_classes import ManageMyTank


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
        self.screen = pg.display.set_mode(self.window_size)

        self.tanks_screen_update = TanksScreen()
        self.player_tank = self.tanks_screen_update.draw_elements(self.screen)

        self.my_tank = ManageMyTank(self.player_tank, self.screen)

        self.key = ""
        self.time_delay = 100

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
                        self.my_tank.turn_my_tank(0)

                    self.my_tank.forward_go(event.key)

                elif event.type == pg.KEYUP and event.key == pg.K_UP:
                    self.key = event.key
                    self.my_tank.forward_stop(self.key)

                elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                    if not self.key == event.key:
                        print("r")
                        self.end_time = pg.time.get_ticks() + self.time_delay
                        self.my_tank.turn_my_tank(-90)

                    self.my_tank.forward_go(event.key)

                elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
                    self.key = event.key
                    self.my_tank.forward_stop(self.key)

                elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                    if not self.key == event.key:
                        print("d")
                        self.end_time = pg.time.get_ticks() + self.time_delay
                        self.my_tank.turn_my_tank(180)

                    self.my_tank.forward_go(event.key)

                elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
                    self.key = event.key
                    self.my_tank.forward_stop(self.key)

                elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                    if not self.key == event.key:
                        print("d")
                        self.end_time = pg.time.get_ticks() + self.time_delay
                        self.my_tank.turn_my_tank(90)

                    self.my_tank.forward_go(event.key)

                elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
                    self.key = event.key
                    self.my_tank.forward_stop(self.key)

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

            self.my_tank.move_image(self.state_key)


if __name__ == "__main__":
    ai = Tanks()
    ai.run_game()
