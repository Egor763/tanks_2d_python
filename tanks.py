import pygame
import grid_bg
import variable
import screen_update


pygame.init()

W = variable.W
H = variable.H


window_size = (W, H)

# задаем название окна
pygame.display.set_caption("Танки")

# создаем окно
screen = pygame.display.set_mode(window_size)

# переазагружаем страницу
screen_update.screen_update(screen)
# pygame.display.update()


# загружаем сохраненный список и кладем в переменную bricks
# bricks = pickle.load(open("save.p", "rb"))

# # пробегаемся по списку с ключом coordinats (так как все координаты лежат именно там) и при
# # каждой итерации получаем brick:  {'x': 660, 'y': 176}
# for brick in bricks["coordinates"].values():
#     # загружаем изображение по ключу image (не меняется)
#     square = pygame.image.load(bricks["image"])
#     # выводится на экран полученным координатам
#     screen.blit(square, (brick["x"], brick["y"]))
# # обновляем экран
# pygame.display.update()

# обновляем экран для отображения изменений
pygame.display.flip()
# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     pg.quit()
        #     exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        # добавляем слушатель при нажатии на клетку
        if event.type == pygame.MOUSEBUTTONDOWN:
            # добавляем кирпич
            if event.pos[0] < 880:
                coord = grid_bg.check_cell(event.pos)
                # вызываем функцию и возвращаем значения и кладем в переменную bricks
                # вызываем функцию add_cell
                if not coord:
                    bricks = grid_bg.add_cell(event.pos, screen)
                # вызываем функцию del_cell и обновляем экран
                else:
                    bricks = grid_bg.del_cell(coord)

                    screen_update.screen_update(screen)
                    pygame.display.update()
            # вызываем функцию get_link_image
            else:
                grid_bg.get_link_image(event.pos)

        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("Мышь нажата:", event.button, "Координаты:", event.pos)

#     # screen.fill((255, 255, 255))
#     # pygame.display.flip()

# pygame.quit()
