import pygame
import random
import time
import sys
from escuela import escuela
from library import library
from restorante import restorante
from cine import cine
from tienda import tienda

screen_width = 1000
screen_with_text = 700
screen_height = 600
def main_game(task_run, x, y):
    pygame.mixer.pre_init(44100, -16, 1, 512)
    # Инициализация Pygame
    pygame.init()

    pygame.mixer.music.load("assets/music.mp3")
    s = pygame.mixer.Sound("assets/catch.ogg")

    # Определение цветов
    WHITE = (255, 255, 255)

    # Установка размеров окна

    screen = pygame.display.set_mode((screen_width, screen_with_text))
    pygame.display.set_caption("Paseo por la ciudad")

    character_width = 77
    character_height = 114

    # Загрузка изображения карты города и персонажа
    city_map = pygame.image.load("assets/city_map.png")
    city_map = pygame.transform.scale(city_map, (screen_width,screen_height))
    character = pygame.image.load("assets/character.png")
    character = pygame.transform.scale(character, (character.get_width() // 6,character.get_height() // 6))
    character_rect = character.get_rect()
    #character_rect.center = (screen_width // 2, screen_height // 2)
    character_rect.x = x
    character_rect.y = y


    def draw_task(string):
        # Отрисовка окна с заданиями
        pygame.draw.rect(screen, (238, 207, 207), (0, screen_height, screen_width, screen_with_text - screen_height))
        pygame.draw.rect(screen, WHITE, (0, screen_height, screen_width, screen_with_text - screen_height), border_radius=50)
        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 32)
        text = font.render(string, True, (255, 145, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_with_text - ((screen_with_text - screen_height) // 2)))
        screen.blit(text, text_rect)

    pygame.mixer.music.play(-1)

    # Основной игровой цикл

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_rect.x -= 1
            if character_rect.x<0:
                character_rect.x += 1
        if keys[pygame.K_RIGHT]:
            character_rect.x += 1
            if character_rect.x>=screen_width-character_width:
                character_rect.x -= 1
        if keys[pygame.K_UP]:
            character_rect.y -= 1
            if character_rect.y<0:
                character_rect.y += 1
        if keys[pygame.K_DOWN]:
            character_rect.y += 1
            if character_rect.y>screen_height-character_height:
                character_rect.y -= 1

        # Отрисовка карты и персонажа
        screen.blit(city_map, (0, 0))
        screen.blit(character, character_rect)



        # Проверка, достиг ли персонаж 1 места на карте
        if task_run==1:
            draw_task("Ir al cine hacia arriba y hacia la izquierda.")
            if character_rect.x > 0 and character_rect.y > 0 and character_rect.x < 100 and character_rect.y <150:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Genial!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                if cine() == 0:
                    main_game(2, character_rect.x, character_rect.y)


        elif task_run==2:
            #draw_task("¡Genial!")
            #
            draw_task("Ir a la escuela derecha y abajo.")
            if character_rect.x > 750 and character_rect.y >160 and character_rect.x < 900 and character_rect.y <250:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Excelente!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                if escuela()==0:
                    main_game(3, character_rect.x, character_rect.y)

        elif task_run==3:
            draw_task("Ir a la biblioteca a la izquierda y hacia abajo.")
            if character_rect.x > 200 and character_rect.y > 350 and character_rect.x < 300 and character_rect.y <450:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Bien hecho!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                if library(1) == 0:
                    main_game(4, character_rect.x, character_rect.y)

        elif task_run==4:
            draw_task("Ir al restaurante hacia arriba y hacia la derecha.")
            if character_rect.x > 430 and character_rect.y > 90 and character_rect.x < 550 and character_rect.y <130:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Correcto!!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                if restorante(1) == 0:
                    main_game(5, character_rect.x, character_rect.y)

        elif task_run==5:
            draw_task("Ir a la tienda hacia abajo y hacia la derecha.")
            if character_rect.x > 800 and character_rect.y > 400 and character_rect.x < 900 and character_rect.y <600:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Genial!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                pygame.mixer.music.stop()
                if tienda() == 0:
                    main_game(1, character_rect.x, character_rect.y)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

main_game(1,screen_width // 2, screen_height // 2)