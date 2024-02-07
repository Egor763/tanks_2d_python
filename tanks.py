import pygame

W = 1050
H = 800
window_size = (W, H)

# задаем название окна
pygame.display.set_caption("Танки")



# создаем окно
screen = pygame.display.set_mode(window_size)

bg = pygame.image.load("assets/images/bg-grass.jpg")
screen.blit(bg, (0, 0))

# обновляем экран для отображения изменений
pygame.display.flip()

# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()