import pygame

from dinamic_obj.ball import Ball
from dinamic_obj.left_paddle import LeftPaddle
# from dinamic_obj.left_paddle_bottom import LeftPaddleBottom
# from dinamic_obj.left_paddle_top import LeftPaddleTop
from dinamic_obj.right_paddle import RightPaddle
from settings import KEY_LEFT, KEY_RIGHT
from static_obj.wall import Wall
from utils import load_image


def main():
    pygame.init()
    pygame.display.set_caption('Столкновение шариков')
    all_sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode((500, 660))
    walls = pygame.sprite.Group()
    shadow = pygame.sprite.Group()

    paddles = pygame.sprite.Group()

    Wall(
        angle=90,
        rebound_ratio=0.91,
        img='images/left_1_bottom_90.png',
        all_sprites=all_sprites,
        walls=walls,
        name='left_1_bottom_90'
    )

    Wall(
        angle=133,
        rebound_ratio=0.91,
        img='images/left_1_main_133.png',
        all_sprites=all_sprites,
        walls=walls,
        name='left_1_main_133'
    )

    Wall(
        angle=270,
        rebound_ratio=0.91,
        img='images/right_1_bottom_270.png',
        all_sprites=all_sprites,
        walls=walls,
        name='right_1_bottom_270'
    )
    Wall(
        angle=223,
        rebound_ratio=0.91,
        img='images/right_1_main_223.png',
        all_sprites=all_sprites,
        walls=walls,
        name='right_1_main_223'
    )

    Wall(
        angle=0,
        rebound_ratio=0.91,
        img='images/top_2_temp_0.png',
        all_sprites=all_sprites,
        walls=walls,
        name='top_2_temp_0'
    )

    Wall(
        angle=270,
        rebound_ratio=0.91,
        img='images/right_2_temp_270.png',
        all_sprites=all_sprites,
        walls=walls,
        name='right_2_temp_270'
    )

    Wall(
        angle=90,
        rebound_ratio=0.91,
        img='images/left_2_temp_90.png',
        all_sprites=all_sprites,
        walls=walls,
        name='left_2_temp_90'
    )

    left_paddle_top = LeftPaddle(
        angle=133,
        kick_ratio=1.2,
        rebound_ratio=0.91,
        img=load_image('sprites/paddle_top_left.png'),
        all_sprites=all_sprites,
        paddles=paddles,
        name='paddle_left_top',
        columns=15,  #!!!
        rows=2  #!!!
    )

    right_paddle_top = RightPaddle(
        angle=223,
        kick_ratio=1.2,
        rebound_ratio=0.91,
        img=load_image('sprites/paddle_top_right.png'),
        all_sprites=all_sprites,
        paddles=paddles,
        name='paddle_right_top',
        columns=15,  # !!!
        rows=2  # !!!
    )

    left_paddle_bottom = LeftPaddle(
        angle=334,
        kick_ratio=1.05,
        rebound_ratio=0.91,
        img=load_image('sprites/paddle_bottom_left.png'),
        paddles=paddles,
        all_sprites=all_sprites,
        name='paddle_left_bottom',
        columns=15,  # !!!
        rows=2  # !!!
    )

    right_paddle_bottom = RightPaddle(
        angle=382,
        kick_ratio=1.05,
        rebound_ratio=0.91,
        img=load_image('sprites/paddle_bottom_right.png'),
        all_sprites=all_sprites,
        paddles=paddles,
        name='paddle_right_bottom',
        columns=15,  # !!!
        rows=2  # !!!
    )

    for i in range(1):
        Ball(20, 200, 200, all_sprites)

    running = True
    rotate = False
    clock = pygame.time.Clock()
    t = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # print(event.key)
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
                    # pass
        screen.fill((40, 40, 40))
        all_sprites.draw(screen)
        t = clock.tick() / 1000
        all_sprites.update(paddles, walls, t, all_sprites, shadow, screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
