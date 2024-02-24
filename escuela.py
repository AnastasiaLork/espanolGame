import pygame
import random

def escuela():
    # Инициализация Pygame
    pygame.init()

    # Определение цветов
    BLACK = (34,46,75)
    WHITE = (238, 207, 207)

    # Определение размеров экрана
    screen_width = 775
    screen_height = 775

    # Определение размеров карточек
    card_width = 190
    card_height = 190

    # Создание окна
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Escuela")


    # Функция для создания игрового поля
    def create_board(rows, cols):
        board = []
        images = []

        for i in range(rows * cols // 2):
            images.append(i)
            images.append(i)

        random.shuffle(images)
        index = 0
        for r in range(rows):
            row = []

            for c in range(cols):
                card = {
                    "image": images[index],
                    "rect": pygame.Rect(c * card_width + 5*c, r * card_height + 5*r, card_width, card_height),
                    "opened": False,
                    "matched": False
                }
                row.append(card)
                index+=1

            board.append(row)


        return board


    # Функция для отрисовки игрового поля
    def draw_board(board):
        for row in board:
            for card in row:
                if card["opened"]:
                    pygame.draw.rect(screen, WHITE, card["rect"])
                    image = card_images[card["image"]]
                    image = pygame.transform.scale(image, (card_width, card_height))
                    image_rect = image.get_rect()
                    image_rect.center = card["rect"].center
                    screen.blit(image, image_rect)
                else:
                    pygame.draw.rect(screen, WHITE, card["rect"])


    # Функция для обработки клика на карточку
    def handle_click(board, row, col):
        card = board[row][col]
        if not card["opened"] and not card["matched"]:
            card["opened"] = True
            draw_board(board)
            pygame.display.update()

            opened_cards = []
            # Проверка, открыты ли уже две карточки
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c]["opened"] and not board[r][c]["matched"]:
                        opened_cards.append((r, c))

            if len(opened_cards) == 2:
                r1, c1 = opened_cards[0]
                r2, c2 = opened_cards[1]
                if board[r1][c1]["image"] == board[r2][c2]["image"]:
                    board[r1][c1]["matched"] = True
                    board[r2][c2]["matched"] = True
                else:
                    pygame.time.delay(600)
                    board[r1][c1]["opened"] = False
                    board[r2][c2]["opened"] = False






    # Загрузка изображений карточек
    card_images = [
        pygame.image.load("assets/escuelaCards/image1.png"),
        pygame.image.load("assets/escuelaCards/image2.png"),
        pygame.image.load("assets/escuelaCards/image3.png"),
        pygame.image.load("assets/escuelaCards/image4.png"),
        pygame.image.load("assets/escuelaCards/image5.png"),
        pygame.image.load("assets/escuelaCards/image6.png"),
        pygame.image.load("assets/escuelaCards/image7.png"),
        pygame.image.load("assets/escuelaCards/image8.png")
        # Загрузите свои изображения или используйте другие
    ]

    # Создание игрового поля
    board = create_board(4, 4)


    # Основной игровой цикл
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    for r in range(len(board)):
                        for c in range(len(board[0])):
                            if board[r][c]["rect"].collidepoint(mouse_pos):
                                handle_click(board, r, c)

        screen.fill(BLACK)
        draw_board(board)
        pygame.display.flip()
        clock.tick(60)

    # Выход из игры
    pygame.quit()
    return 0
#escuela()