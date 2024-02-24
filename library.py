import pygame

screen_width = 1000
screen_height = 800

def library(number_page):
    # Инициализация Pygame
    pygame.init()
    page_active = number_page-1
    # Установка размеров окна

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Biblioteca")

    # Загрузка изображений карточек
    page_images = [
        pygame.image.load("assets/libro/page1.png"),
        pygame.image.load("assets/libro/page2.png"),
        pygame.image.load("assets/libro/page3.png"),
        pygame.image.load("assets/libro/page4.png"),
        pygame.image.load("assets/libro/page5.png"),
        pygame.image.load("assets/libro/page6.png"),
        pygame.image.load("assets/libro/page7.png"),
        pygame.image.load("assets/libro/page8.png"),
    ]

    def draw_page(number_page):
        page = page_images[number_page]
        page = pygame.transform.scale(page, (screen_width, screen_height))
        screen.blit(page, (0, 0))
    # Определение размеров и положения кнопки
    button_width = 70
    button_height = 70
    button_x = screen_width - button_width
    button_y = screen_height // 2

    # Определение размеров и положения 2 кнопки
    button2_width = 70
    button2_height = 70
    button2_x = 0
    button2_y = screen_height // 2


    # Функция для отображения кнопки
    def draw_button(page_active):
        if page_active == 0:
            pygame.draw.rect(screen, (255, 224, 169), (button_x, button_y, button_width, button_height), border_radius=50)
            font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 50)
            text = font.render("→", True, (0, 0, 0))
            text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
            screen.blit(text, text_rect)
        elif page_active == 7:
            pygame.draw.rect(screen, (255, 224, 169), (button2_x, button2_y, button2_width, button2_height), border_radius=50)
            font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 50)
            text = font.render("←", True, (0, 0, 0))
            text_rect = text.get_rect(center=(button2_x + button2_width // 2, button2_y + button2_height // 2))
            screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, (255, 224, 169), (button_x, button_y, button_width, button_height),
                             border_radius=50)
            font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 50)
            text = font.render("→", True, (0, 0, 0))
            text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
            screen.blit(text, text_rect)

            pygame.draw.rect(screen, (255, 224, 169), (button2_x, button2_y, button2_width, button2_height),
                             border_radius=50)
            font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 50)
            text = font.render("←", True, (0, 0, 0))
            text_rect = text.get_rect(center=(button2_x + button2_width // 2, button2_y + button2_height // 2))
            screen.blit(text, text_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    if page_active <7:
                        page_active+=1
                elif button2_x <= mouse_x <= button2_x + button2_width and button2_y <= mouse_y <= button2_y + button2_height:
                    if page_active >0:
                        page_active-=1


        draw_page(page_active)

        # Отображение кнопки
        draw_button(page_active)

        pygame.display.flip()

    pygame.quit()
    return 0
