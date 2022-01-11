from math import degrees, asin, pi, acos, sqrt
from typing import Union, List

import pygame

from utils.lib import load_image


class Bumper(pygame.sprite.Sprite):
    """
    Класс для создания бампера.
    """

    def __init__(
        self,
        center_circle: List[Union[int, float]],
        img: str,
        all_sprites: pygame.sprite.Group,
        bumpers: pygame.sprite.Group,
        name: str,
        rebound_ratio: int,
        x: int = 0,
        y: int = 0,
    ) -> None:
        super().__init__(all_sprites)
        self.add(bumpers)
        self.name = name

        self.rebound_ratio = rebound_ratio
        self.rebound_sound = pygame.mixer.Sound('src/sounds/rebound_1.mp3')

        self.center_circle = center_circle

        self.image = load_image(img)
        if self.image:
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

            self.rect.x = x
            self.rect.y = y

    def creation_angle(self, ball: pygame.sprite.Sprite) -> None:
        """
        Метод создаёт угол касательной исходя из координат центра банки
        и координат центра мячика.

        :param ball: спрайт мячик
        :return: Создаёт угол касательной мяча и краски
        """
        x_ball, y_ball = ball.x + ball.radius, ball.y + ball.radius
        x_blot, y_blot = self.center_circle

        x_vector, y_vector = x_blot - x_ball, y_blot - y_ball

        vector_len = sqrt(x_vector ** 2 + y_vector ** 2)

        # если вектор направлен в 1-ю координатную четверть
        if x_vector > 0 and y_vector <= 0:
            vector_sin = -y_vector / vector_len
            vector_angle = asin(vector_sin)

        # если вектор направлен в 2-ю координатную четверть
        elif x_vector <= 0 and y_vector < 0:
            vector_cos = x_vector / vector_len
            vector_angle = acos(vector_cos)

        # если вектор направлен в 3-ю координатную четверть
        elif x_vector < 0 and y_vector >= 0:
            vector_cos = x_vector / vector_len
            vector_angle = -acos(vector_cos)
            vector_angle += pi * 2  # вычисляем размер угла из отрицательного

        # если вектор направлен в 4-ю координатную четверть
        elif x_vector >= 0 and y_vector > 0:
            vector_sin = -y_vector / vector_len
            vector_angle = asin(vector_sin)
            vector_angle += pi * 2  # вычисляем размер угла из отрицательного

        self.angle = degrees(vector_angle - (pi / 2))  # перпендикуляр
        if self.angle < 0:
            self.angle += 360  # Отрицательный угол нам не подходит
