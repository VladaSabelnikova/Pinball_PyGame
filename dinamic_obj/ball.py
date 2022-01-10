import random
from math import sqrt
from typing import Callable

import pygame

from dinamic_obj.shadow import Shadow
from utils.lib import load_image, get_reflected_vector, \
    get_reflected_vector_paddle, get_reflected_vector_blot, \
    get_reflected_vector_bumper
from utils.settings import SIMPLE_GRAVITY, BALL_PATH, MAX_SPEED, SOUND_GAP, \
    SOUND_VOLUME_CONTROL


class Ball(pygame.sprite.Sprite):
    """
    Класс для создания мячика.
    """

    def __init__(
        self,
        radius: int,
        gravity: int = SIMPLE_GRAVITY
    ) -> None:

        super().__init__()
        self.radius = radius

        self.gravity = gravity

        image = load_image(BALL_PATH)
        self.image = pygame.transform.scale(image, (radius * 2, radius * 2))
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        self.previous_barrier = None

        self.position_creation()
        self.time_from_last_sound = SOUND_GAP

    def position_creation(self) -> None:
        """
        Метод создаёт стартовую позицию мяча и вектор его направления.
        """
        self.x = random.randint(1, 41)
        self.y = random.randint(-40, 0)

        self.vx = random.randint(-250, 250)
        self.vy = 0

    def update(
        self,
        paddles: pygame.sprite,
        walls: pygame.sprite,
        blots: pygame.sprite.Group,
        bumpers: pygame.sprite.Group,
        t: float,
        all_sprites: pygame.sprite.Group,
        shadow: pygame.sprite.Group,
        screen: pygame.display
    ) -> None:

        """
        Метод перерисовывает тень и
        генерирует поиск collide всех препятствий по маске.

        :param paddles: — группа со всеми лопатками
        :param walls:  — группа со всеми стенами
        :param blots: — группа со всеми красками
        :param bumpers: — группа со всеми препятствиями
        :param t: — время, прошедшее с момента последнего update
        :param all_sprites: — группа, где лежат все спрайты
        :param shadow: — группа со всеми следами теней
        :param screen: — полотно, на котором мы рисуем
        :return: его задача нарисовать очередной след от тени,
        пройти по всем поверхностям и, в зависимости от того
         с чем именно столкнулся мячик, изменить вектор.
        """

        self.x += self.vx * t
        self.y += self.vy * t

        self.vy += self.gravity * t

        self.time_from_last_sound += t

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # Создаём очередную тень.
        Shadow(all_sprites, shadow, self.x, self.y)

        # Тень должна быть ниже на слой относительно мяча.
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # Поиск столкновений с различными типами препятствий.
        # В метод new_vector мы передадим группу препятствий
        # и функцию, которая должна высчитывать новый вектор.
        self.new_vector(walls, get_reflected_vector)
        self.new_vector(paddles, get_reflected_vector_paddle)
        self.new_vector(blots, get_reflected_vector_blot)
        self.new_vector(bumpers, get_reflected_vector_bumper)

    def new_vector(
        self, collide_surface: pygame.sprite, func: Callable
    ) -> None:
        """
        Метод выявляет столкновение с препятствием и заменяет вектор.
        """

        # Проверяем столкновение по маске.
        # В collides будут лежать объекты, с которыми столкнулся мячик.
        collides = pygame.sprite.spritecollide(
            self,
            collide_surface,
            False,
            collided=pygame.sprite.collide_mask
        )

        # Если столкновение есть —
        # проходим по всем поверхностям и заменяем направление вектора.
        if collides:
            for barrier in collides:

                # func — функция счёта, которую мы передали аргументом.
                temp_x, temp_y = func(
                    [self.vx, self.vy],
                    barrier,
                    self.previous_barrier == barrier,
                    self
                )
                # Если вектор изменил направление
                if (temp_x, temp_y) != (self.vx, self.vy):
                    vector_len = sqrt(temp_x ** 2 + temp_y ** 2)
                    if vector_len > MAX_SPEED:
                        speed_ratio = MAX_SPEED / vector_len
                        temp_x = temp_x * speed_ratio
                        temp_y = temp_y * speed_ratio

                    self.vx, self.vy = temp_x, temp_y
                    self.previous_barrier = barrier

                    if self.time_from_last_sound >= SOUND_GAP:
                        # Изменяем громкость в зависимости от силы удара
                        volume = (temp_x ** 2 + temp_y ** 2) / SOUND_VOLUME_CONTROL
                        barrier.rebound_sound.set_volume(volume)
                        barrier.rebound_sound.play()
                        self.time_from_last_sound = 0
                    break
