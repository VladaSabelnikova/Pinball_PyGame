import pygame.sprite

from utils.settings import BUMP_REBOUND_RATIO_LATERAL, \
    BUMP_REBOUND_RATIO_CENTER
from static_obj.bumper import Bumper


def add_center_bumper(
    all_sprites: pygame.sprite.Group,
    bumpers: pygame.sprite.Group
) -> None:
    """
    Функция создаёт центральный отбойник
    :param all_sprites: группа со всеми спрайтами
    :param bumpers: группа со всеми отбойниками
    :return: Создаст центральный бампер, чтобы можно было вставить его
    на уровень отдельно от остальных.
    """
    Bumper(
        center_circle=[250, 330],
        img='images/bumper_center_250_330.png',
        all_sprites=all_sprites,
        bumpers=bumpers,
        name='bumper_center_250_330',
        rebound_ratio=BUMP_REBOUND_RATIO_CENTER
    )


def add_lateral_bumper(
    all_sprites: pygame.sprite.Group,
    bumpers: pygame.sprite.Group
) -> None:
    """
    Функция создаёт боковые отбойники
    :param all_sprites: группа со всеми спрайтами
    :param bumpers: группа со всеми отбойниками
    :return: Создаст боковые отбойники, чтобы можно было вставить их
    на уровень отдельно от остальных.
    """
    Bumper(
        center_circle=[-270, 307],
        img='images/bumper_left_-270_307.png',
        all_sprites=all_sprites,
        bumpers=bumpers,
        name='bumper_left_-270_307',
        rebound_ratio=BUMP_REBOUND_RATIO_LATERAL
    )

    Bumper(
        center_circle=[770, 307],
        img='images/bumper_right_770_307.png',
        all_sprites=all_sprites,
        bumpers=bumpers,
        name='bumper_right_770_307',
        rebound_ratio=BUMP_REBOUND_RATIO_LATERAL
    )
