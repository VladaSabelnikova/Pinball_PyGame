import random
from typing import Tuple

import pygame

from dinamic_obj.shadow import Shadow
from settings import GRAVITY, BALL_PATH
from utils import load_image, get_reflected_vector, logger


class Ball(pygame.sprite.Sprite):
    """
    Класс для создания мячика.
    """

    def __init__(
        self,
        radius: int,
        x: int,
        y: int,
        all_sprites: pygame.sprite.Group
    ) -> None:

        super().__init__(all_sprites)
        self.radius = radius

        image = load_image(BALL_PATH)
        self.image = pygame.transform.scale(image, (radius * 2, radius * 2))
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        # Рандомное направление вектора.
        self.vx = random.randint(-2000, 2000)
        self.vy = random.randint(-2000, -1500)
        self.x = x
        self.y = y

    def update(
        self,
        walls: pygame.sprite,
        t: float,
        all_sprites: pygame.sprite.Group,
        shadow: pygame.sprite.Group,
        screen: pygame.display,
    ) -> None:

        self.x += self.vx * t
        self.y += self.vy * t

        self.vy += GRAVITY * t

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # Создаём очередную тень.
        Shadow(all_sprites, shadow, self.x, self.y)

        # Тень должна быть ниже на слой относительно мяча.
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # Проверяем столкновение по маске.
        collides_walls = pygame.sprite.spritecollide(
            self,
            walls,
            False,
            collided=pygame.sprite.collide_mask
        )

        # collides_paddles = pygame.sprite.spritecollide(
        #     self,
        #     paddles,
        #     False,
        #     collided=pygame.sprite.collide_mask
        # )

        if collides_walls:  # Если столкновение есть —
            # проходим по всем поверхностями заменяем направление вектора.
            for wall in collides_walls:
                logger.debug(f'{wall.name} {wall.angle}')
                self.vx, self.vy = get_reflected_vector(
                    [self.vx, self.vy],
                    wall.angle,
                    wall.rebound_ratio
                )

        # if collides_paddles:
        #     for paddle in collides_paddles:
        #         logger.debug(f'{paddle.name} {paddle.angle}')
        #         self.vx, self.vy = get_reflected_vector(
        #             [self.vx, self.vy],
        #             paddle.angle,
        #             paddle.rebound_ratio
        #         )
