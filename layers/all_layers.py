import pygame

from dinamic_obj.ball import Ball
from layers.all_blots import add_blots
from layers.all_bumpers import add_lateral_bumper, add_center_bumper
from layers.all_paddles import creation_paddles
from layers.all_walls import add_walls
from layers.game_loop import game_loop
from layers.general_settings_for_game import creation_general_settings
from utils.settings import SIMPLE_GRAVITY, \
    AVERAGE_GRAVITY, NIGHTMARE_GRAVITY


def simple():
    """
    Функция создаёт уровень игры — "Тренировка".
    :return: Вернёт кол-во набранных очков.
    """

    # Создаём фоновую музыку для этого уровня.
    pygame.mixer.music.load('src/sounds/simple_theme.mp3')

    # Создаём общие для всех уровней инициализирующие настройки.
    all_sprites, screen, shadow, \
    paddles, bumpers, blots, walls = creation_general_settings()

    # Для этого уровня нам потребуются все стенки,
    # все банки с красками,
    # все лопатки.
    add_walls(all_sprites, walls)
    add_blots(all_sprites, blots)

    left_paddle_top, right_paddle_top, \
    left_paddle_bottom, right_paddle_bottom = creation_paddles(
        all_sprites,
        paddles
    )

    # Ну и мячик, с легкой гравитацией.
    ball = Ball(20, gravity=SIMPLE_GRAVITY)

    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    # Результат игрового цикла — кол-во набранных очков.
    result = game_loop(
        all_sprites,
        left_paddle_top,
        left_paddle_bottom,
        right_paddle_top,
        right_paddle_bottom,
        screen,
        paddles,
        walls,
        blots,
        bumpers,
        shadow,
        ball
    )

    pygame.mixer.music.stop()

    # Результат уровня — кол-во очков, набранных в игровом цикле.
    return result


def average():
    """
    Функция создаёт уровень игры — "Игра".
    :return: Вернёт кол-во набранных очков.
    """

    # Создаём фоновую музыку для этого уровня.
    pygame.mixer.music.load('src/sounds/average_theme.mp3')

    # Создаём общие для всех уровней инициализирующие настройки.
    all_sprites, screen, shadow, \
    paddles, bumpers, blots, walls = creation_general_settings()

    # Для этого уровня нам потребуются все стенки,
    # все банки с красками,
    # все лопатки
    # и боковые отбойники.
    add_walls(all_sprites, walls)
    add_blots(all_sprites, blots)
    add_lateral_bumper(all_sprites, bumpers)

    left_paddle_top, right_paddle_top, \
    left_paddle_bottom, right_paddle_bottom = creation_paddles(all_sprites,
                                                               paddles)

    # Ну и мячик, со средней гравитацией.
    ball = Ball(20, gravity=AVERAGE_GRAVITY)

    pygame.mixer.music.set_volume(0.23)
    pygame.mixer.music.play(-1)

    # Результат игрового цикла — кол-во набранных очков.
    result = game_loop(
        all_sprites,
        left_paddle_top,
        left_paddle_bottom,
        right_paddle_top,
        right_paddle_bottom,
        screen,
        paddles,
        walls,
        blots,
        bumpers,
        shadow,
        ball
    )

    pygame.mixer.music.stop()
    # Результат уровня — кол-во очков, набранных в игровом цикле.
    return result


def nightmare():
    """
    Функция создаёт уровень игры — "NIGHTMARE".
    :return: Вернёт кол-во набранных очков.
    """

    # Создаём фоновую музыку для этого уровня.
    pygame.mixer.music.load('src/sounds/nightmare_theme.mp3')

    # Создаём общие для всех уровней инициализирующие настройки.
    all_sprites, screen, shadow, \
    paddles, bumpers, blots, walls = creation_general_settings()

    # Для этого уровня нам потребуются все стенки,
    # все банки с красками,
    # все лопатки
    # боковые отбойники,
    # центральный круглый отбойник.
    add_walls(all_sprites, walls)
    add_lateral_bumper(all_sprites, bumpers)
    add_center_bumper(all_sprites, bumpers)
    add_blots(all_sprites, blots)

    left_paddle_top, right_paddle_top, \
    left_paddle_bottom, right_paddle_bottom = creation_paddles(
        all_sprites,
        paddles
    )

    # Ну и мячик, со сложной гравитацией.
    ball = Ball(20, gravity=NIGHTMARE_GRAVITY)

    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    # Результат игрового цикла — кол-во набранных очков.
    result = game_loop(
        all_sprites,
        left_paddle_top,
        left_paddle_bottom,
        right_paddle_top,
        right_paddle_bottom,
        screen,
        paddles,
        walls,
        blots,
        bumpers,
        shadow,
        ball
    )
    pygame.mixer.music.stop()

    # Результат уровня — кол-во очков, набранных в игровом цикле.
    return result
