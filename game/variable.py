from pygame.locals import *

W = 924
H = 704
w_cell = 44
h_cell = 44
green = (0, 255, 0)
LEFT = "right"
player_tank = {}
FPS = 60


my_tank = "game/assets/images/tanks/tank_my.png"

key2mvmt = {K_UP: False, K_DOWN: False, K_LEFT: False, K_RIGHT: False}
