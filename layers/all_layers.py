import pygame

from dinamic_obj.ball import Ball
from layers.all_blots import add_blots
from layers.all_bumpers import add_lateral_bumper, add_center_bumper
from layers.all_paddles import creation_paddles
from layers.all_walls import add_walls
from layers.general_settings_for_game import creation_general_settings
from settings import KEY_LEFT, KEY_RIGHT, BALL_PAUSE, SIMPLE_GRAVITY, \
    AVERAGE_GRAVITY, NIGHTMARE_GRAVITY, EXTRA_BALLS
from utils import result_calculation


def simple():
    all_sprites, screen, shadow, \
    paddles, bumpers, blots, walls = creation_general_settings()

    add_walls(all_sprites, walls)
    add_blots(all_sprites, blots)

    left_paddle_top, right_paddle_top, \
    left_paddle_bottom, right_paddle_bottom = creation_paddles(all_sprites,  paddles)

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
    left_paddle_bottom, right_paddle_bottom = creation_paddles(all_sprites,  paddles)

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


def game_loop(
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
):
    ball_pause = BALL_PAUSE
    extra_balls = EXTRA_BALLS

    rotate = False
    clock = pygame.time.Clock()
    t = None
    game_time = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                rotate = True
                if event.key == KEY_LEFT:
                    left_paddle_top.rotate_up = rotate
                    left_paddle_bottom.rotate_up = rotate
                elif event.key == KEY_RIGHT:
                    right_paddle_top.rotate_up = rotate
                    right_paddle_bottom.rotate_up = rotate

            if event.type == pygame.KEYUP:
                rotate = False
                if event.key == KEY_LEFT:
                    left_paddle_top.rotate_up = rotate
                    left_paddle_bottom.rotate_up = rotate
                elif event.key == KEY_RIGHT:
                    right_paddle_top.rotate_up = rotate
                    right_paddle_bottom.rotate_up = rotate
        screen.fill((40, 40, 40))
        all_sprites.draw(screen)
        t = clock.tick() / 1000
        game_time += t
        all_blots_broken = all([blot.broken for blot in blots.sprites()])
        if not ball.groups() and not all_blots_broken:
            ball_pause -= t
            if ball_pause <= 0:
                ball_pause = BALL_PAUSE
                ball.position_creation()
                ball.add(all_sprites)
        if all_blots_broken:  # победа
            ball_pause -= t
            if ball_pause <= 0:
                return result_calculation(game_time, extra_balls)
        if ball.y >= 700:  # лузер
            ball_pause -= t
            if ball_pause <= 0:
                if extra_balls:
                    ball_pause = BALL_PAUSE
                    extra_balls -= 1
                    ball.position_creation()
                else:
                    return -1
        all_sprites.update(paddles, walls, blots, bumpers, t, all_sprites,
                           shadow, screen)
        pygame.display.flip()
    pygame.quit()
