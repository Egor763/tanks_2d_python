import pygame as pg
import variable
from tanks_screen_classes import TanksScreen
from manage_my_tank_classes import ManageMyTank
from fire import Fire


class Tanks:
    def __init__(self):
        pg.init()

        self.W = variable.W
        self.H = variable.H
        self.fire_width = variable.fire_width
        self.fire_height = variable.fire_height

        self.FPS = variable.FPS
        self.end_time = 0
        self.delay_fire = variable.delay_fire
        self.delay_move_tank = variable.delay_move_tank

        self.key = ""
        self.state_key = False
        self.key_fire = False
        self.key2mvmt = variable.key2mvmt

        self.link_my_tank = variable.my_tank
        self.FPS_CLOCK = pg.time.Clock()
        self.timer_event = pg.USEREVENT
        self.tank_shot_sound = pg.mixer.Sound(
            "game/assets/sounds/Sound/tank_fire_bullet.ogg"
        )

        self.window_size = (self.W, self.H)

        pg.display.set_caption("Танки")
        self.screen = pg.display.set_mode(self.window_size)

        self.tanks_screen_update = TanksScreen()
        self.player_tank = self.tanks_screen_update.draw_elements(self.screen)
        self.my_tank = ManageMyTank(self.player_tank, self.screen)
        self.fires = pg.sprite.Group()

        pg.display.flip()

    # функция создания класса выстрела (вызывается при каждом выстреле)
    def fire_bullet(self):
        new_fire = Fire(self.screen, self.player_tank)
        self.fires.add(new_fire)

    def run_game(self):
        while True:
            # скорость цикла
            self.FPS_CLOCK.tick(self.FPS)
            # создание текущего времени
            self.current_time = pg.time.get_ticks()

            self.fires.update()

            self.tanks_screen_update.handle_image_screen(self.screen)

            for event in pg.event.get():
                # == КНОПКА ВВЕРХ ==========================================================
                if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                    if not self.key == event.key:
                        print("u")
                        self.end_time = pg.time.get_ticks() + self.delay_move_tank
                        self.my_tank.turn_my_tank(0)

                    self.my_tank.forward_go(event.key)
                # -----------------------------------------------------------------
                elif event.type == pg.KEYUP and event.key == pg.K_UP:
                    self.key = event.key
                    self.my_tank.forward_stop(self.key)

                # ==== КНОПКА ВПРАВО =========================================================
                elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                    if not self.key == event.key:
                        print("r")
                        self.end_time = pg.time.get_ticks() + self.delay_move_tank
                        self.my_tank.turn_my_tank(-90)

                    self.my_tank.forward_go(event.key)
                # -------------------------------------------------------------------
                elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
                    self.key = event.key
                    self.my_tank.forward_stop(self.key)

                # ======== КНОПКА ВНИЗ ===============================================
                elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                    if not self.key == event.key:
                        print("d")
                        self.end_time = pg.time.get_ticks() + self.delay_move_tank
                        self.my_tank.turn_my_tank(180)

                    self.my_tank.forward_go(event.key)

                # ---------------------------------------------------
                elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
                    self.key = event.key
                    self.my_tank.forward_stop(self.key)

                # ====== КНОПКА ВЛЕВО ==========================================
                elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                    if not self.key == event.key:
                        print("d")
                        self.end_time = pg.time.get_ticks() + self.delay_move_tank
                        self.my_tank.turn_my_tank(90)

                    self.my_tank.forward_go(event.key)

                # ---------------------------------------------------
                elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
                    self.key = event.key
                    self.my_tank.forward_stop(self.key)

                # == ПРОБЕЛ ============================================
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.key_fire = True
                    self.tank_shot_sound.play()
                    self.fire_bullet()
                    pg.time.set_timer(self.timer_event, self.delay_fire)

                # ---------------------------------------------------
                elif event.type == pg.KEYUP and event.key == pg.K_SPACE:
                    self.key_fire = False

                # == ВЫСТРЕЛ ТАНКА С ЗАДЕРЖКОЙ ========================
                elif event.type == self.timer_event and self.key_fire:
                    self.tank_shot_sound.play()
                    self.fire_bullet()

                # == ВЫХОД ИЗ ИГРЫ ===============
                elif event.type == pg.QUIT:
                    pg.quit()
                    exit()

                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    exit()

            # == отрисовка одного из нескольких выстрелов ======
            for fire in self.fires.sprites():
                fire.draw_fire()

            # == задержка времени поворота танка =========
            if self.current_time < self.end_time:
                self.state_key = True
            else:
                self.state_key = False

            # == движение танка ==============
            self.my_tank.move_image(self.state_key)


if __name__ == "__main__":
    ai = Tanks()
    ai.run_game()
