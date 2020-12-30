# Nombre: Luis Alejandro Martinez
# Matricula: 20197725


# Setup Python ----------------------------------------------- #
from pygame.locals import *
import pygame
import sys
import os
import random
import time
from random import randint
from pygame import mixer


# Setup pygame/window ---------------------------------------- #
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = WIDTH, HEIGHT
mainClock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)

pygame.display.set_caption('CARRERA PRESIDENCIAL')
icon = pygame.image.load("imgs/icon.png")
pygame.display.set_icon(icon)

font = pygame.font.SysFont(None, 20)
buttonFont = pygame.font.SysFont(None, 64)
title_font = pygame.font.SysFont(None, 64)


global player


def player(img, x, y):
    screen.blit(img, (x, y))


def update_player():
    random_number = randint(1, 2)
    return random_number


def draw_line(img, x, y):
    screen.blit(img, (x, y))


def play_sound(sound_file):
    mixer.music.load(sound_file)
    mixer.music.play()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def create_button(msg, color_Text, button_color, x, y, button_width, button_height):
    textRect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, button_color, textRect)
    draw_text(msg, buttonFont, color_Text, screen, x +
              (button_width / 2), y + (button_height / 2))
    return textRect


def main_menu():
    os.system('cls')
    click = False
    play_button_color = (250, 255, 255)
    while True:

        screen.fill((0, 0, 0))
        draw_text('CARRERA PRESIDENCIAL', title_font,
                  (255, 255, 255), screen, WIDTH/2, 60)

        mx, my = pygame.mouse.get_pos()

        button_1 = create_button(
            "PLAY", (0, 255, 0), play_button_color,  250, HEIGHT/2, 300, 80)

        if button_1.collidepoint((mx, my)):
            play_button_color = (250, 0, 0)
            if click:
                options()
        else:
            play_button_color = (250, 255, 255)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    race_status = "pause"
    YOU_VOTO = 1

    START_POSITION = 10

    #  CANDIDATO1
    CANDIDATO1_IMG = pygame.image.load("imgs/candidato1.png")
    CANDIDATO1_X = START_POSITION
    CANDIDATO1_Y = 0

    #  CANDIDATO2
    CANDIDATO2_IMG = pygame.image.load("imgs/candidato2.png")
    CANDIDATO2_X = START_POSITION
    CANDIDATO2_Y = 150

    #  CANDIDATO3
    CANDIDATO3_IMG = pygame.image.load("imgs/candidato3.png")
    CANDIDATO3_X = START_POSITION
    CANDIDATO3_Y = 300

    #  CANDIDATO4
    CANDIDATO4_IMG = pygame.image.load("imgs/candidato4.png")
    CANDIDATO4_X = START_POSITION
    CANDIDATO4_Y = 500

    #  LINE
    LINE_IMG = pygame.image.load("imgs/line.png")
    LINE_X = 700
    LINE_Y = 0

    # VOTOS
    CANDIDATO1_VOTOS = 10
    CANDIDATO2_VOTOS = 10
    CANDIDATO3_VOTOS = 10
    CANDIDATO4_VOTOS = 10

    someone_won = False
    narracion_sound = "sounds/narracion.wav"
    CANDIDATO2_sound = "sounds/leonel_voto.wav"
    CANDIDATO1_sound = "sounds/abinader_voto.wav"
    CANDIDATO3_sound = "sounds/gonzalo_voto.wav"
    CANDIDATO4_sound = "sounds/guillermo_voto.wav"

    CANDIDATO1_win_sound = "sounds/abinader_win.wav"
    CANDIDATO2_win_sound = "sounds/leonel_win.wav"
    CANDIDATO3_win_sound = "sounds/gonzalo_win.wav"
    CANDIDATO4_win_sound = "sounds/guillermo_win.wav"

    background_sound_start = True
    win_sound_start = True
    lose_sound_start = True
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_line(LINE_IMG, LINE_X, LINE_Y)

        draw_text(f'VOTOS: {CANDIDATO1_VOTOS}', font,
                  (255, 255, 255), screen, 370, 50)
        draw_text(f'VOTOS: {CANDIDATO2_VOTOS}', font,
                  (12, 204, 36), screen, 370, 200)
        draw_text(f'VOTOS: {CANDIDATO3_VOTOS}', font,
                  (140, 9, 239), screen, 370, 350)
        draw_text(f'VOTOS: {CANDIDATO4_VOTOS}', font,
                  (0, 247, 178), screen, 370, 550)

        # Handler for quit the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # KEY Handler
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        if race_status == "running":
            CANDIDATO1_X += update_player()
            CANDIDATO2_X += update_player()
            CANDIDATO3_X += update_player()
            CANDIDATO4_X += update_player()

            if CANDIDATO1_X >= WIDTH - 100:
                CANDIDATO1_VOTOS += 10
                CANDIDATO2_VOTOS -= 5
                CANDIDATO3_VOTOS -= 5
                CANDIDATO4_VOTOS -= 5

                play_sound(CANDIDATO1_sound)
                CANDIDATO1_X = START_POSITION
                CANDIDATO2_X = START_POSITION
                CANDIDATO3_X = START_POSITION
                CANDIDATO4_X = START_POSITION

            if CANDIDATO2_X >= WIDTH - 100:
                CANDIDATO2_VOTOS += 10
                CANDIDATO1_VOTOS -= 5
                CANDIDATO3_VOTOS -= 5
                CANDIDATO4_VOTOS -= 5

                play_sound(CANDIDATO2_sound)
                CANDIDATO2_X = START_POSITION
                CANDIDATO1_X = START_POSITION
                CANDIDATO3_X = START_POSITION
                CANDIDATO4_X = START_POSITION

            if CANDIDATO3_X >= WIDTH - 100:
                CANDIDATO3_VOTOS += 10
                CANDIDATO1_VOTOS -= 5
                CANDIDATO2_VOTOS -= 5
                CANDIDATO4_VOTOS -= 5

                play_sound(CANDIDATO3_sound)
                CANDIDATO3_X = START_POSITION
                CANDIDATO1_X = START_POSITION
                CANDIDATO2_X = START_POSITION
                CANDIDATO4_X = START_POSITION

            if CANDIDATO4_X >= WIDTH - 100:
                CANDIDATO4_VOTOS += 10
                CANDIDATO1_VOTOS -= 5
                CANDIDATO2_VOTOS -= 5
                CANDIDATO3_VOTOS -= 5

                play_sound(CANDIDATO4_sound)
                CANDIDATO4_X = START_POSITION
                CANDIDATO1_X = START_POSITION
                CANDIDATO2_X = START_POSITION
                CANDIDATO3_X = START_POSITION

        if someone_won == False:
            race_status = "running"
            if background_sound_start:
                play_sound(narracion_sound)

        CANDIDATO1 = "abinader"
        CANDIDATO2 = "leonel"
        CANDIDATO3 = "gonzalo"
        CANDIDATO4 = "guillermo"

        if player == CANDIDATO1:
            YOU_VOTO = CANDIDATO1_VOTOS
            YOU_win_sound = CANDIDATO1_win_sound
        if player == CANDIDATO2:
            YOU_VOTO = CANDIDATO2_VOTOS
            YOU_win_sound = CANDIDATO2_win_sound
        if player == CANDIDATO3:
            YOU_VOTO = CANDIDATO3_VOTOS
            YOU_win_sound = CANDIDATO3_win_sound
        if player == CANDIDATO4:
            YOU_VOTO = CANDIDATO4_VOTOS
            YOU_win_sound = CANDIDATO4_win_sound

        if YOU_VOTO <= 0:
            if lose_sound_start:
                lose_sound_start = False
                play_sound("sounds/perdio.wav")

            draw_text('PERDISTE!', title_font,
                      (255, 255, 255), screen, 370, HEIGHT / 2)
            race_status = "pause"
            time.sleep(3)
            running = False

        if YOU_VOTO >= 50:
            draw_text('GANASTE ERES EL PRESIDENTE!', title_font,
                      (255, 255, 255), screen, 370, HEIGHT / 2)
            if win_sound_start:
                win_sound_start = False
                play_sound(YOU_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO1_VOTOS >= 50:
            if win_sound_start:
                win_sound_start = False
                draw_text('CANDITATO 1 WON', title_font,
                          (255, 255, 255), screen, 370, HEIGHT / 2)
                play_sound(CANDIDATO1_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO2_VOTOS >= 50:
            if win_sound_start:
                win_sound_start = False
                draw_text('CANDITATO 2 WON', title_font,
                          (255, 255, 255), screen, 370, HEIGHT / 2)
                play_sound(CANDIDATO2_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO3_VOTOS >= 50:
            if win_sound_start:
                win_sound_start = False
                draw_text('CANDITATO 3 WON', title_font,
                          (255, 255, 255), screen, 370, HEIGHT / 2)
                play_sound(CANDIDATO3_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO4_VOTOS >= 50:
            if win_sound_start:
                win_sound_start = False
                draw_text('CANDITATO 4 WON', title_font,
                          (255, 255, 255), screen, 370, HEIGHT / 2)
                play_sound(CANDIDATO4_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO1_VOTOS == 0 and CANDIDATO2_VOTOS == 0 and CANDIDATO3_VOTOS == 0:
            if win_sound_start:
                win_sound_start = False
                draw_text('CANDITATO 4 WON', title_font,
                          (255, 255, 255), screen, 370, HEIGHT / 2)
                play_sound(CANDIDATO4_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO1_VOTOS == 0 and CANDIDATO2_VOTOS == 0 and CANDIDATO4_VOTOS == 0:
            if win_sound_start:
                win_sound_start = False
                draw_text('CANDITATO 3 WON', title_font,
                          (255, 255, 255), screen, 370, HEIGHT / 2)
                play_sound(CANDIDATO3_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO1_VOTOS == 0 and CANDIDATO4_VOTOS == 0 and CANDIDATO3_VOTOS == 0:
            if win_sound_start:
                win_sound_start = False
                draw_text('CANDITATO 2 WON', title_font,
                          (255, 255, 255), screen, 370, HEIGHT / 2)
                play_sound(CANDIDATO2_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO4_VOTOS == 0 and CANDIDATO2_VOTOS == 0 and CANDIDATO3_VOTOS == 0:
            if win_sound_start:
                win_sound_start = False
                draw_text('CANDITATO 1 WON', title_font,
                          (255, 255, 255), screen, 370, HEIGHT / 2)
                play_sound(CANDIDATO1_win_sound)
                time.sleep(3)
                running = False
                race_status = "pause"
                someone_won = True

        if CANDIDATO1_VOTOS <= 0:
            CANDIDATO1_X = 0
            CANDIDATO1_VOTOS = 0
        if CANDIDATO2_VOTOS <= 0:
            CANDIDATO2_X = 0
            CANDIDATO2_VOTOS = 0
        if CANDIDATO3_VOTOS <= 0:
            CANDIDATO3_X = 0
            CANDIDATO3_VOTOS = 0
        if CANDIDATO4_VOTOS <= 0:
            CANDIDATO4_X = 0
            CANDIDATO4_VOTOS = 0

        player(CANDIDATO1_IMG, CANDIDATO1_X, CANDIDATO1_Y)
        player(CANDIDATO2_IMG, CANDIDATO2_X, CANDIDATO2_Y)
        player(CANDIDATO3_IMG, CANDIDATO3_X, CANDIDATO3_Y)
        player(CANDIDATO4_IMG, CANDIDATO4_X, CANDIDATO4_Y)
        background_sound_start = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    click = False
    go_button_color = (250, 255, 255)
    player_1_color = (250, 0, 0)
    player_2_color = (250, 0, 0)
    player_3_color = (250, 0, 0)
    player_4_color = (250, 0, 0)
    player_1_color_letter = (255, 0, 0)
    player_2_color_letter = (255, 0, 0)
    player_3_color_letter = (255, 0, 0)
    player_4_color_letter = (255, 0, 0)

    player_1_x = 200
    player_2_x = 200
    player_3_x = 200
    player_4_x = 200

    while running:
        screen.fill((0, 0, 0))
        draw_text('options', font, (255, 255, 255), screen, 20, 20)

        # INSTRUCTIONS
        draw_text("TIENE QUE SELECCIONAR EL CANDIDATO DE TU PREFERENCIA.",
                  font, (255, 255, 255), screen, 400, 40)
        draw_text("SI GANA LA CARRERA OBTINES 10 VOTOS Y SINO PIERDES 5 VOTOS",
                  font, (255, 255, 255), screen, 400, 60)
        draw_text("SI LLEGAS A 0 VOTOS PIERDES Y SI LLEGAS A 50 VOTOS ERES EL PRESIDENTE!",
                  font, (255, 255, 255), screen, 400, 80)

        msg = create_button(
            "Click En Tu Candidato:", (255, 255, 255), (0, 0, 0),  200, 100, 400, 40)

        player_1 = create_button(
            "Luis Abinader", player_1_color_letter, player_1_color,  player_1_x, 200, 400, 40)
        player_2 = create_button(
            "Leonel Fernandez", player_2_color_letter, player_2_color,  player_2_x, 250, 400, 40)
        player_3 = create_button(
            "Gonzalo Castillo", player_3_color_letter, player_3_color, player_3_x, 300, 400, 40)
        player_4 = create_button(
            "Guillermo Moreno", player_4_color_letter, player_4_color, player_4_x, 350, 400, 40)

        play_button = create_button(
            "GO", (0, 255, 0), go_button_color,  200, HEIGHT/2 + 200, 400, 80)

        mx, my = pygame.mouse.get_pos()

        if play_button.collidepoint((mx, my)):
            go_button_color = (250, 0, 0)

            if click:
                print(player)
                game()
        else:
            go_button_color = (250, 255, 255)

        if player_1.collidepoint((mx, my)):
            player_1_color = (250, 255, 255)
            player_1_color_letter = (255, 0, 0)

            if click:
                player_1_x = 250
                player_2_x = 200
                player_3_x = 200
                player_4_x = 200
                player = "abinader"

        else:
            player_1_color = (250, 0, 0)
            player_1_color_letter = (250, 255, 255)

        if player_2.collidepoint((mx, my)):
            player_2_color = (250, 255, 255)
            player_2_color_letter = (255, 0, 0)

            if click:
                player_2_x = 250
                player_1_x = 200
                player_3_x = 200
                player_4_x = 200
                player = "leonel"

        else:
            player_2_color = (250, 0, 0)
            player_2_color_letter = (250, 255, 255)

        if player_3.collidepoint((mx, my)):
            player_3_color_letter = (255, 0, 0)
            player_3_color = (250, 255, 255)

            if click:
                player_3_x = 250
                player_1_x = 200
                player_2_x = 200
                player_4_x = 200
                player = "gonzalo"

        else:
            player_3_color = (250, 0, 0)
            player_3_color_letter = (250, 255, 255)

        if player_4.collidepoint((mx, my)):
            player_4_color = (250, 255, 255)
            player_4_color_letter = (255, 0, 0)

            if click:
                player_4_x = 250
                player_1_x = 200
                player_2_x = 200
                player_3_x = 200
                player = "guillermo"

        else:
            player_4_color = (250, 0, 0)
            player_4_color_letter = (250, 255, 255)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


main_menu()


# Nombre: Luis Alejandro Martinez
# Matricula: 20197725
