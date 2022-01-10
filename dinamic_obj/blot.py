from math import sqrt, asin, acos, pi, degrees
from typing import Union, Tuple

import pygame

from utils.settings import BLOT_SPEED


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

        self.speed = BLOT_SPEED
        self.static_rebound_ratio = rebound_ratio
        self.rebound_sound = pygame.mixer.Sound('src/sounds/rebound_1.mp3')

        self.breaking_sound = pygame.mixer.Sound('src/sounds/breaking_blot.mp3')
        self.breaking_sound.set_volume(.5)

        self.broken = False
        self.angle = None

        self.fall_coefficient = .95

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
        *_, t = args[:5]
        old_frame = self.cur_frame
        if self.broken:
            self.cur_frame += self.speed * t
            self.cur_frame = min(self.cur_frame, len(self.frames) - 1)
            self.image = self.frames[int(self.cur_frame)]
            self.mask = pygame.mask.from_surface(self.image)

            if int(old_frame) != int(self.cur_frame):
                self.speed = max(self.fall_coefficient * self.speed, 16)
                self.fall_coefficient **= 2

    def creation_angle(self, ball: pygame.sprite.Sprite) -> None:
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

        self.angle = degrees(vector_angle - (pi / 2))
        if self.angle < 0:
            self.angle += 360
        print('blot.angle — ', self.angle)