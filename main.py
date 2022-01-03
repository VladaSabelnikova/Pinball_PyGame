import pygame

from dinamic_obj.ball import Ball
from static_obj.wall import Wall


def main():
    pygame.init()
    pygame.display.set_caption('Столкновение шариков')
    all_sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode((500, 660))
    walls = pygame.sprite.Group()
    shadow = pygame.sprite.Group()

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


    Wall(10, 0.93, 'images/top_10.png', all_sprites, walls, 'top')
    # Wall(190, 0.93, 'images/bott_190.png', all_sprites, walls, 'bott', 0, 411)
    #
    Wall(100, 0.93, 'images/left_100.png', all_sprites, walls, 'left')
    Wall(280, 0.93, 'images/right_280.png', all_sprites, walls, 'right', 411, 0)

    for i in range(1):
        Ball(20, 200, 200, all_sprites)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((40, 40, 40))
        all_sprites.draw(screen)
        t = clock.tick() / 1000
        print(t)
        all_sprites.update(walls, t, all_sprites, shadow, screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
