import pygame
import time

# Определение цветов
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (34, 145, 169)
ROSA = (224, 175, 160)
YELLOW = (255, 140, 0)


screen_width = 1000
screen_height = 800

def tienda():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    # Инициализация Pygame
    pygame.init()

    si = pygame.mixer.Sound("assets/catch.ogg")
    no = pygame.mixer.Sound("assets/no.ogg")

    # Установка размеров окна
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tienda")

    # Загрузка фонового изображения
    fon = pygame.image.load("assets/tienda/magasin.png")
    fon = pygame.transform.scale(fon, (screen_width, screen_height))

    # Определение размеров карточек
    card_width = 150
    card_height = 150

    # Загрузка изображений карточек
    card_images = [
        pygame.image.load("assets/tienda/1.png"),
        pygame.image.load("assets/tienda/2.png"),
        pygame.image.load("assets/tienda/3.png"),
        pygame.image.load("assets/tienda/4.png"),
        pygame.image.load("assets/tienda/5.png"),
        pygame.image.load("assets/tienda/6.png"),
        pygame.image.load("assets/tienda/7.png"),
        pygame.image.load("assets/tienda/8.png"),
        pygame.image.load("assets/tienda/9.png"),
        pygame.image.load("assets/tienda/10.png"),
        pygame.image.load("assets/tienda/11.png"),
        pygame.image.load("assets/tienda/12.png"),
        pygame.image.load("assets/tienda/13.png"),
        pygame.image.load("assets/tienda/14.png"),
        pygame.image.load("assets/tienda/15.png")
    ]

    # Задание
    substrate_width = 900
    substrate_height = 120

    # Задание
    audio_width = 100
    audio_height = 100

    # Загрузка фонового изображения
    audio_jpg = pygame.image.load("assets/tienda/speaker.png")
    audio_jpg = pygame.transform.scale(audio_jpg, (audio_width-20, audio_height-20))

    audio_task = pygame.mixer.Sound("assets/tienda/1.wav")

    answer = [
        [(0, 0), (0, 1), (1, 3)],
        [(0, 4), (1, 2)],
        [(2, 1), (2, 2), (1, 4)],
        [(0, 2), (1, 1)],
        [(0, 3)]
    ]

    # Функция для создания игрового поля
    def create_board(rows, cols):
        board = []

        index = 0
        interval_cards = 14
        start_pos_x = (screen_width - (card_width*cols+interval_cards*cols)) // 2
        start_pos_y = 100

        for r in range(rows):
            row = []
            for c in range(cols):
                card = {
                    "image": index,
                    "rect": pygame.Rect(c*card_width + interval_cards*c + start_pos_x,
                                        r*card_height + interval_cards*r + start_pos_y,
                                        card_width,
                                        card_height),
                    "guessed": False,
                    "notcorrect": False
                }
                row.append(card)
                index+=1

            board.append(row)
        return board

    # Функция для отрисовки игрового поля
    def draw_board(board):
        border = 8
        for row in board:
            for card in row:
                if card["guessed"]:
                    pygame.draw.rect(screen, GREEN, card["rect"])
                    image = card_images[card["image"]]
                    image = pygame.transform.scale(image, (card_width-border, card_height-border))
                    image_rect = image.get_rect()
                    image_rect.center = card["rect"].center
                    screen.blit(image, image_rect)
                elif card["notcorrect"]:
                    pygame.draw.rect(screen, RED, card["rect"])
                    image = card_images[card["image"]]
                    image = pygame.transform.scale(image, (card_width-border, card_height-border))
                    image_rect = image.get_rect()
                    image_rect.center = card["rect"].center
                    screen.blit(image, image_rect)
                else:
                    pygame.draw.rect(screen, WHITE, card["rect"])
                    image = card_images[card["image"]]
                    image = pygame.transform.scale(image, (card_width - border, card_height - border))
                    image_rect = image.get_rect()
                    image_rect.center = card["rect"].center
                    screen.blit(image, image_rect)

    # Функция для обработки клика на карточку
    def handle_click(board, r, c, number_quetion):
        number_quetion-=1
        mismatch = 0
        for i in range(len(answer[number_quetion])):
            r1, c1 = answer[number_quetion][i]
            if board[r][c] == board[r1][c1]:
                board[r][c]["guessed"] = True
                si.play()
                draw_board(board)
                return 1
            else:
                mismatch+=1
        if mismatch == len(answer[number_quetion]):
            no.play()
            board[r][c]["notcorrect"] = True
        draw_board(board)
        return 0

    def draw_number_task(color,number):

        # Отрисовка номера задания
        pygame.draw.rect(screen, color, (20, 20, 70, 70), border_radius=40)

        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 40)
        text = font.render(str(number), True, WHITE)
        text_rect = text.get_rect(center=(55, 55))
        screen.blit(text, text_rect)

    def draw_task():
        start_pos_x = (screen_width - substrate_width) // 2
        # Отрисовка окна с заданиями
        pygame.draw.rect(screen, WHITE, (start_pos_x, 640, substrate_width, substrate_height), border_radius=20)

        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 26)
        text = font.render("Escucha el audio y elige qué productos", True, (0, 0, 0))
        text_rect = text.get_rect(center=(350, 680))
        screen.blit(text, text_rect)
        text = font.render("quiere comprar Lucía.                 ", True, (0, 0, 0))
        text_rect = text.get_rect(center=(350, 710))
        screen.blit(text, text_rect)
        draw_audio()

    def draw_audio():
        # Отрисовка окна с заданиями
        pygame.draw.rect(screen, ROSA, (830, 650, audio_width, audio_height), border_radius=60)
        screen.blit(audio_jpg, (840, 660))


    # Создание игрового поля
    board = create_board(3, 5)

    number_correct_answers = 0
    number_quetion = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 840 <= mouse_x <= 940 and 660 <= mouse_y <= 760:
                        audio_task.play()
                    for r in range(len(board)):
                        for c in range(len(board[0])):
                            if board[r][c]["rect"].collidepoint(mouse_pos):
                                if handle_click(board, r, c,number_quetion):
                                    number_correct_answers+=1
                                pygame.display.update()
                                time.sleep(0.8)
                                for r in range(len(board)):
                                    for c in range(len(board[0])):
                                        board[r][c]["notcorrect"] = False
                                draw_board(board)
                                if number_quetion == 1:
                                    if number_correct_answers == 3:
                                        number_quetion+=1
                                        number_correct_answers = 0
                                        time.sleep(0.6)
                                        for r in range(len(board)):
                                            for c in range(len(board[0])):
                                                board[r][c]["guessed"] = False
                                        draw_board(board)
                                elif number_quetion == 2:
                                    if number_correct_answers == 2:
                                        number_quetion+=1
                                        number_correct_answers = 0
                                        time.sleep(0.6)
                                        for r in range(len(board)):
                                            for c in range(len(board[0])):
                                                board[r][c]["guessed"] = False
                                        draw_board(board)
                                elif number_quetion == 3:
                                    if number_correct_answers == 3:
                                        number_quetion+=1
                                        number_correct_answers = 0
                                        time.sleep(0.6)
                                        for r in range(len(board)):
                                            for c in range(len(board[0])):
                                                board[r][c]["guessed"] = False
                                        draw_board(board)
                                elif number_quetion == 4:
                                    if number_correct_answers == 2:
                                        number_quetion+=1
                                        number_correct_answers = 0
                                        time.sleep(0.6)
                                        for r in range(len(board)):
                                            for c in range(len(board[0])):
                                                board[r][c]["guessed"] = False
                                        draw_board(board)
                                elif number_quetion == 5:
                                    if number_correct_answers == 1:
                                        number_quetion=1
                                        number_correct_answers = 0
                                        time.sleep(0.6)
                                        for r in range(len(board)):
                                            for c in range(len(board[0])):
                                                board[r][c]["guessed"] = False
                                        draw_board(board)



        screen.blit(fon, (0, 0))
        draw_board(board)

        if number_quetion == 1:
            draw_number_task(BLUE,1)
            draw_task()
            audio_task = pygame.mixer.Sound("assets/tienda/1.wav")
        elif number_quetion == 2:
            draw_number_task(YELLOW, 2)
            draw_task()
            audio_task = pygame.mixer.Sound("assets/tienda/2.wav")
        elif number_quetion == 3:
            draw_number_task(ROSA, 3)
            draw_task()
            audio_task = pygame.mixer.Sound("assets/tienda/3.wav")
        elif number_quetion == 4:
            draw_number_task(BLUE, 4)
            draw_task()
            audio_task = pygame.mixer.Sound("assets/tienda/4.wav")
        elif number_quetion == 5:
            draw_number_task(YELLOW, 5)
            draw_task()
            audio_task = pygame.mixer.Sound("assets/tienda/5.wav")


        pygame.display.flip()

    # Выход из игры
    pygame.quit()
    return 0

#tienda()
