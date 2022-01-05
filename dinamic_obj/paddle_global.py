from typing import Union

import pygame

from settings import PADDLE_SPEED


class PaddleGlobal(pygame.sprite.Sprite):
    """
    Класс, общий для всех досок и их частей.
    Только общие атрибуты и методы для всех, ничего лишнего.
    """

    def __init__(
        self,
        angle: int,
        rebound_ratio: Union[int, float],
        kick_ratio: float,  # Вот он
        img: pygame.image,
        paddles: pygame.sprite.Group,
        all_sprites: pygame.sprite.Group,
        name: str,
        columns: int,
        rows: int,
        x: int = 0,
        y: int = 0,
    ) -> None:

        super().__init__(paddles)
        self.add(all_sprites)
        self.name = name
        self.start_angle = angle
        self.start_rebound_ratio = rebound_ratio

        self.angle = angle
        self.rebound_ratio = rebound_ratio

        self.frames = []
        self.cut_sheet(img, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.rotate_up = False

        self.speed = PADDLE_SPEED
        self.kick_ratio = kick_ratio
        self.static_rebound_ratio = rebound_ratio

    def cut_sheet(
        self,
        sheet: pygame.image,
        columns: int = 3,
        rows: int = 1
    ) -> None:

        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        if 'left' in self.name.split('_'):
            self.frames = self.frames[::-1]
