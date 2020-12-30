import pygame,sys
import random
from random import randint



DESCRIPTION = "Este juego se trata de una carrera entre candidatos a presidente"
CANDIDATO1 = "Luis Abinader"
CANDIDATO2 = "Leonel Fernandez"
CANDIDATO3 = "Gonzalo Castillo"
CANDIDATO4 = "Guillermo Moreno"

# SCREEN
WIDTH = 800
HEIGHT = 600
START_POSITION = 10
SCREEN_SIZE = WIDTH, HEIGHT
race_status = "pause"
screen = pygame.display.set_mode(SCREEN_SIZE)

# Title and Icon
pygame.display.set_caption("CARRERA PRESIDENCIAL")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#  CANDIDATO1
CANDIDATO1_IMG = pygame.image.load("candidato1.png")
CANDIDATO1_X = START_POSITION
CANDIDATO1_Y = 0
CANDIDATO1_X_CHANGE = 0
CANDIDATO1_Y_CHANGE = 0
#  CANDIDATO2
CANDIDATO2_IMG = pygame.image.load("candidato2.png")
CANDIDATO2_X = START_POSITION
CANDIDATO2_Y = 150
CANDIDATO2_X_CHANGE = 0
CANDIDATO2_Y_CHANGE = 0
#  CANDIDATO3
CANDIDATO3_IMG = pygame.image.load("candidato3.png")
CANDIDATO3_X = START_POSITION
CANDIDATO3_Y = 300
CANDIDATO3_X_CHANGE = 0
CANDIDATO3_Y_CHANGE = 0
#  CANDIDATO4
CANDIDATO4_IMG = pygame.image.load("candidato4.png")
CANDIDATO4_X = START_POSITION
CANDIDATO4_Y = 500
CANDIDATO4_X_CHANGE = 0
CANDIDATO4_Y_CHANGE = 0
#  LINE
LINE_IMG = pygame.image.load("line.png")
LINE_X = 700
LINE_Y = 0


def player(img, x, y):
    screen.blit(img, (x, y))


def update_player():
    random_number = randint(1, 2)
    return random_number


def draw_line():
    screen.blit(LINE_IMG, (LINE_X, LINE_Y))


# GAME LOOP
running = True
while running:
    # backgroundColor
    screen.fill((0, 0, 0))
    draw_line()
    # Handler for quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEY Handler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                CANDIDATO1_X = -0.1

            if event.key == pygame.K_RIGHT:
                CANDIDATO1_X = 0.1
        # if event.type == pygame.KEYUP:
            # if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                # CANDIDATO1_X = 0
                # CANDIDATO2_X = 0

    if race_status == "running":
        CANDIDATO1_X += update_player()
        CANDIDATO2_X += update_player()
        CANDIDATO3_X += update_player()
        CANDIDATO4_X += update_player()

        if CANDIDATO1_X >= WIDTH - 100:
            print("CANDIDATO1 WON")
            CANDIDATO1_X = 700
            race_status = "pause"
        if CANDIDATO2_X >= WIDTH - 100:
            print("CANDIDATO2 WON")
            CANDIDATO2_X = 700
            race_status = "pause"
        if CANDIDATO3_X >= WIDTH - 100:
            print("CANDIDATO3 WON")
            CANDIDATO3_X = 700
            race_status = "pause"
        if CANDIDATO4_X >= WIDTH - 100:
            print("CANDIDATO4 WON")
            CANDIDATO4_X = 700
            race_status = "pause"

    if CANDIDATO1_X != 700 and CANDIDATO2_X != 700 and CANDIDATO3_X != 700 and CANDIDATO4_X != 700:
        race_status = "running"

    player(CANDIDATO1_IMG, CANDIDATO1_X, CANDIDATO1_Y)
    player(CANDIDATO2_IMG, CANDIDATO2_X, CANDIDATO2_Y)
    player(CANDIDATO3_IMG, CANDIDATO2_X, CANDIDATO3_Y)
    player(CANDIDATO4_IMG, CANDIDATO4_X, CANDIDATO4_Y)

    pygame.display.update()




