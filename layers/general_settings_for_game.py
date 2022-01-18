from typing import Tuple

import pygame


def creation_general_settings() -> Tuple:
    """

    Функция создаёт общие для всех уровней настройки.

    :return: Возвращает необходимые для игры параметры
    """
    pygame.init()
    pygame.mixer.init(buffer=8192)
    pygame.display.set_caption('Игра')
    all_sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode((500, 660))
    shadow = pygame.sprite.Group()

    paddles = pygame.sprite.Group()
    bumpers = pygame.sprite.Group()
    blots = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    return all_sprites, screen, shadow, paddles, bumpers, blots, walls
