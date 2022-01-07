import random
from math import sqrt

import pygame

from dinamic_obj.shadow import Shadow
from settings import GRAVITY, BALL_PATH, MAX_SPEED
from utils import load_image, get_reflected_vector, logger, \
    get_reflected_vector_paddle, get_reflected_vector_blot


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
        # self.vx = random.randint(-2000, 2000)
        # self.vy = random.randint(-2000, -1500)
        # self.vx = random.randint(-500, 500)
        # self.vy = random.randint(-500, 500)

        self.vx = -1000
        self.vy = -1200

        self.previous_barrier = None

        self.x = 0
        self.y = 200

    def update(
        self,
        paddles: pygame.sprite,
        walls: pygame.sprite,
        blots,
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
        self.new_vector(walls, get_reflected_vector)
        self.new_vector(paddles, get_reflected_vector_paddle)
        self.new_vector(blots, get_reflected_vector_blot)

    def new_vector(self, collide_surface: pygame.sprite, func) -> None:

        """
        Метод выявляет столкновение с препятствием и заменяет вектор.
        """

        # Проверяем столкновение по маске.
        collides = pygame.sprite.spritecollide(
            self,
            collide_surface,
            False,
            collided=pygame.sprite.collide_mask
        )

        # Если столкновение есть —
        # проходим по всем поверхностям и заменяем направление вектора.
        if collides: #and self.was_a_jump:
            for barrier in collides:
                # logger.debug(f'{barrier.name} {barrier.angle}')
                temp_x, temp_y = func(
                    [self.vx, self.vy],
                    barrier,
                    self.previous_barrier == barrier,
                    self
                )
                if (temp_x, temp_y) != (self.vx, self.vy):
                    vector_len = sqrt(temp_x ** 2 + temp_y ** 2)
                    if vector_len > MAX_SPEED:
                        speed_ratio = MAX_SPEED / vector_len
                        temp_x = temp_x * speed_ratio
                        temp_y = temp_y * speed_ratio

                    self.vx, self.vy = temp_x, temp_y
                    self.previous_barrier = barrier
                    break
