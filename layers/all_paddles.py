from typing import Tuple

import pygame.sprite

from dinamic_obj.left_paddle import LeftPaddle
from dinamic_obj.right_paddle import RightPaddle
from utils.lib import load_image


def creation_paddles(
    all_sprites: pygame.sprite.Group,
    paddles: pygame.sprite.Group
) -> Tuple[LeftPaddle, RightPaddle, LeftPaddle, RightPaddle]:
    """
    Функция создаст и вернёт все части лопаток.

    :param all_sprites: группа со всеми спрайтами
    :param paddles: группа со всеми частями лопаток
    :return: Вернёт именованные спрайты, части лопаток.
    Мы их именуем, так как они нам потребуются в игровом цикле.
    """

    left_paddle_top = LeftPaddle(
        angle=133,
        rebound_ratio=0.96,
        img=load_image('sprites/paddle_top_left.png'),
        all_sprites=all_sprites,
        paddles=paddles,
        name='paddle_left_top',
        columns=15,
        rows=2
    )

    right_paddle_top = RightPaddle(
        angle=223,
        rebound_ratio=0.96,
        img=load_image('sprites/paddle_top_right.png'),
        all_sprites=all_sprites,
        paddles=paddles,
        name='paddle_right_top',
        columns=15,
        rows=2
    )

    left_paddle_bottom = LeftPaddle(
        angle=334,
        rebound_ratio=0.96,
        img=load_image('sprites/paddle_bottom_left.png'),
        paddles=paddles,
        all_sprites=all_sprites,
        name='paddle_left_bottom',
        columns=15,
        rows=2
    )

    right_paddle_bottom = RightPaddle(
        angle=382,
        rebound_ratio=0.96,
        img=load_image('sprites/paddle_bottom_right.png'),
        all_sprites=all_sprites,
        paddles=paddles,
        name='paddle_right_bottom',
        columns=15,
        rows=2
    )

    return \
        left_paddle_top, \
        right_paddle_top, \
        left_paddle_bottom, \
        right_paddle_bottom
