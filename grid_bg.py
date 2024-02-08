import pygame as pg
import variable


W = variable.W
H = variable.H


def handle_grid(screen):
    # горизонтальная линия
    y = 1
    x = 1

    while y < H:
        pg.draw.line(screen, variable.green, (0, y), (W, y), 1)
        y = y + variable.h_cell

    while x < W:
        pg.draw.line(screen, variable.green, (x, 0), (x, H), 1)
        x = x + variable.w_cell


# square_1 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_1, (88, 44))

# square_2 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_2, (132, 44))

# square_3 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_3, (44, 88))

# square_4 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_4, (88, 88))

# square_5 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_5, (132, 88))

# square_6 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_6, (44, 176))

# square_7 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_7, (88, 176))

# square_8 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_8, (132, 176))

# square_9 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_9, (44, 220))

# square_10 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_10, (88, 220))

# square_11 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_11, (132, 220))

# square_12 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_12, (44, 308))

# square_13 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_13, (88, 308))

# square_14 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_14, (132, 308))

# square_15 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_15, (44, 352))

# square_16 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_16, (88, 352))

# square_17 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_17, (132, 352))

# square_18 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_18, (44, 396))

# square_19 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_19, (88, 396))

# square_20 = pg.image.load("assets/images/bricks_block.png")
# screen.blit(square_20, (132, 396))
