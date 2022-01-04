import pygame

from dinamic_obj.ball import Ball
from dinamic_obj.paddle import Paddle
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

    # Paddle(
    #     angle=223,
    #     rebound_ratio=0.99,
    #     img=load_image('sprites/paddle_right.png'),
    #     all_sprites=all_sprites,
    #     walls=paddles,
    #     name='paddle_right',
    #     columns=3,
    #     rows=1
    # )
    #
    # Paddle(
    #     angle=133,
    #     rebound_ratio=0.99,
    #     img=load_image('sprites/paddle_left.png'),
    #     all_sprites=all_sprites,
    #     walls=paddles,
    #     name='paddle_left',
    #     columns=3,
    #     rows=1
    # )

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
            # if event.type == pygame.KEYDOWN:
            #     rotate = True
            #     paddles.update(is_rotate=rotate)
            # if event.type == pygame.KEYUP:
            #     rotate = False
            #     paddles.update(is_rotate=rotate)
        screen.fill((40, 40, 40))
        all_sprites.draw(screen)
        t = clock.tick() / 1000
        all_sprites.update(walls, t, all_sprites, shadow, screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
