import pygame

from settings import KEY_LEFT, KEY_RIGHT, BALL_PAUSE, EXTRA_BALLS, KEY_UP, \
    KEY_DOWN
from utils.lib import result_calculation, draw_paddle_speed, draw_number_balls


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

    speed_change = 0
    skills_ratio = []

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
                    left_paddle_bottom.working_sound.play()
                if event.key == KEY_RIGHT:
                    right_paddle_top.rotate_up = rotate
                    right_paddle_bottom.rotate_up = rotate
                    right_paddle_bottom.working_sound.play()
                if event.key == KEY_UP:
                    speed_change = 3
                if event.key == KEY_DOWN:
                    speed_change = -3
            if event.type == pygame.KEYUP:
                rotate = False
                if event.key == KEY_LEFT:
                    left_paddle_top.rotate_up = rotate
                    left_paddle_bottom.rotate_up = rotate
                    left_paddle_bottom.working_sound.play()
                if event.key == KEY_RIGHT:
                    right_paddle_top.rotate_up = rotate
                    right_paddle_bottom.rotate_up = rotate
                    right_paddle_bottom.working_sound.play()
                if event.key == KEY_UP or event.key == KEY_DOWN:
                    speed_change = 0
        screen.fill((40, 40, 40))
        all_sprites.draw(screen)
        draw_number_balls(screen, extra_balls)
        draw_paddle_speed(screen, left_paddle_top.speed)
        t = clock.tick() / 1000
        game_time += t

        if speed_change:
            left_paddle_top.set_speed(speed_change)
            left_paddle_bottom.set_speed(speed_change)
            right_paddle_top.set_speed(speed_change)
            right_paddle_bottom.set_speed(speed_change)

        all_blots_broken = all([blot.broken for blot in blots.sprites()])
        if not ball.groups() and not all_blots_broken:
            ball_pause -= t
            if ball_pause <= 0:
                skills_ratio.append(left_paddle_top.speed)
                ball_pause = BALL_PAUSE
                ball.position_creation()
                ball.add(all_sprites)
        if all_blots_broken:  # победа
            ball_pause -= t
            if ball_pause <= 0:
                return result_calculation(game_time, extra_balls, skills_ratio)
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
