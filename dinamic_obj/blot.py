from math import sqrt, asin, acos, pi
from typing import Union, Tuple

import pygame

from settings import PADDLE_SPEED


class Blot(pygame.sprite.Sprite):

    def __init__(
        self,
        center_circle: Tuple[Union[int, float], Union[int, float]],
        rebound_ratio: Union[int, float],
        img: pygame.image,
        blots: pygame.sprite.Group,
        all_sprites: pygame.sprite.Group,
        name: str,
        columns: int,
        rows: int,
        x: int = 0,
        y: int = 0,
        angle=0
    ) -> None:

        super().__init__(blots)
        self.add(all_sprites)
        self.name = name

        self.rebound_ratio = rebound_ratio
        self.center_circle = center_circle

        self.frames = []
        self.cut_sheet(img, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = PADDLE_SPEED
        self.kick_ratio = 1.07 * PADDLE_SPEED / 200
        self.static_rebound_ratio = rebound_ratio

        self.was_collision = False
        self.angle = None

    def cut_sheet(
        self,
        sheet: pygame.image,
        columns: int = 2,
        rows: int = 1
    ) -> None:

        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        if self.was_collision:
            self.cur_frame = min(self.cur_frame + 1, len(self.frames) - 1)
            self.image = self.frames[int(self.cur_frame)]
            self.mask = pygame.mask.from_surface(self.image)

    def creation_angle(self, ball) -> None:
        x_ball, y_ball = ball.x + ball.radius, ball.y + ball.radius
        x_blot, y_blot = self.center_circle

        x_vector, y_vector = x_blot - x_ball, y_blot - y_ball

        vector_len = sqrt(x_vector ** 2 + y_vector ** 2)

        if x_vector > 0 and y_vector <= 0:  # если вектор направлен в 1-ю координатную четверть
            vector_sin = -y_vector / vector_len
            vector_angle = asin(vector_sin)

        elif x_vector <= 0 and y_vector < 0:  # если вектор направлен в 2-ю координатную четверть
            vector_cos = x_vector / vector_len
            vector_angle = acos(vector_cos)

        elif x_vector < 0 and y_vector >= 0:  # если вектор направлен в 3-ю координатную четверть
            vector_cos = x_vector / vector_len
            vector_angle = -acos(vector_cos)
            vector_angle += pi * 2  # вычисляем размер угла из отрицательного

        elif x_vector >= 0 and y_vector > 0:  # если вектор направлен в 4-ю координатную четверть
            vector_sin = -y_vector / vector_len
            vector_angle = asin(vector_sin)
            vector_angle += pi * 2  # вычисляем размер угла из отрицательного

        self.angle = vector_angle + (pi / 2)
