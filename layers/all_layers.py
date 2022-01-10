from dinamic_obj.ball import Ball
from layers.all_blots import add_blots
from layers.all_bumpers import add_lateral_bumper, add_center_bumper
from layers.all_paddles import creation_paddles
from layers.all_walls import add_walls
from layers.game_loop import game_loop
from layers.general_settings_for_game import creation_general_settings
from settings import SIMPLE_GRAVITY, \
    AVERAGE_GRAVITY, NIGHTMARE_GRAVITY


def simple():
    all_sprites, screen, shadow, \
    paddles, bumpers, blots, walls = creation_general_settings()

    add_walls(all_sprites, walls)
    add_blots(all_sprites, blots)

    left_paddle_top, right_paddle_top, \
    left_paddle_bottom, right_paddle_bottom = creation_paddles(all_sprites,
                                                               paddles)

    ball = Ball(20, gravity=SIMPLE_GRAVITY)

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

    return result


def average():
    all_sprites, screen, shadow, \
    paddles, bumpers, blots, walls = creation_general_settings()

    add_walls(all_sprites, walls)
    add_blots(all_sprites, blots)
    add_lateral_bumper(all_sprites, bumpers)

    left_paddle_top, right_paddle_top, \
    left_paddle_bottom, right_paddle_bottom = creation_paddles(all_sprites,
                                                               paddles)

    ball = Ball(20, gravity=AVERAGE_GRAVITY)

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

    return result


def nightmare():
    all_sprites, screen, shadow, \
    paddles, bumpers, blots, walls = creation_general_settings()

    add_walls(all_sprites, walls)
    add_lateral_bumper(all_sprites, bumpers)
    add_center_bumper(all_sprites, bumpers)
    add_blots(all_sprites, blots)

    left_paddle_top, right_paddle_top, \
    left_paddle_bottom, right_paddle_bottom = creation_paddles(all_sprites,
                                                               paddles)

    ball = Ball(20, gravity=NIGHTMARE_GRAVITY)

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

    return result
