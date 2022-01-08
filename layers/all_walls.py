import pygame

from static_obj.wall import Wall


def add_walls(all_sprites, walls):
    Wall(
            angle=90,
            rebound_ratio=0.91,
            img='images/left_1_bottom_90.png',
            all_sprites=all_sprites,
            walls=walls,
            name='left_1_bottom_90'
        )

    Wall(
        angle=158,
        rebound_ratio=0.91,
        img='images/left_1_triangle_158.png',
        all_sprites=all_sprites,
        walls=walls,
        name='left_1_triangle_158'
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
        angle=202,
        rebound_ratio=0.91,
        img='images/right_1_triangle_202.png',
        all_sprites=all_sprites,
        walls=walls,
        name='right_1_triangle_202'
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
