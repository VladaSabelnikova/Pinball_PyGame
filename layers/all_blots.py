import pygame.sprite

from dinamic_obj.blot import Blot
from utils.lib import load_image


def add_blots(
    all_sprites: pygame.sprite.Group,
    blots: pygame.sprite.Group
) -> None:
    """
    Функция создаёт все цветные банки
    :param all_sprites: группа со всеми спрайтами
    :param blots: группа со всеми цветными банками
    :return: Банки создаются безымянными, в программе нигде не вызываются
    """
    Blot(
        center_circle=(250, 100),
        rebound_ratio=0.81,
        img=load_image('sprites/blot_250_100.png'),
        blots=blots,
        all_sprites=all_sprites,
        name='blot_250_100',
        columns=9,
        rows=2
    )

    Blot(
        center_circle=(106, 100),
        rebound_ratio=0.81,
        img=load_image('sprites/blot_106_100.png'),
        blots=blots,
        all_sprites=all_sprites,
        name='blot_106_100',
        columns=9,
        rows=2
    )

    Blot(
        center_circle=(394, 100),
        rebound_ratio=0.81,
        img=load_image('sprites/blot_394_100.png'),
        blots=blots,
        all_sprites=all_sprites,
        name='blot_394_100',
        columns=9,
        rows=2
    )
