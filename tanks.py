import pygame
import grid_bg
import variable


pygame.init()

W = variable.W
H = variable.H


window_size = (W, H)

# задаем название окна
pygame.display.set_caption("Танки")

# создаем окно
screen = pygame.display.set_mode(window_size)

# получаем картинку и сохраняем в переменную
bg = pygame.image.load("assets/images/bg-grass.jpg")
screen.blit(bg, (0, 0))

grid_bg.handle_grid(screen)
# обновляем экран для отображения изменений
pygame.display.flip()

# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     pg.quit()
        #     exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Мышь нажата:", event.button, "Координаты:", event.pos)
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
