from typing import Union

import pygame

from utils.settings import PADDLE_SPEED, PADDLE_SPEED_RANGE


class PaddleGlobal(pygame.sprite.Sprite):
    """
    Класс, общий для всех досок и их частей.
    Только общие атрибуты и методы для всех, ничего лишнего.
    """

    def __init__(
        self,
        angle: int,
        rebound_ratio: Union[int, float],
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
        self.rebound_sound = pygame.mixer.Sound('src/sounds/rebound_1.mp3')
        self.working_sound = pygame.mixer.Sound('src/sounds/paddle_sound.mp3')
        self.working_sound.set_volume(0.7)

        self.frames = []
        self.cut_sheet(img, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.rotate_up = False

        self.speed = PADDLE_SPEED
        self.set_kick_ratio()
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

    def set_kick_ratio(self):
        """
        Метод устанавливает силу толчка лопатки в зависимости от её скорости.
        """
        self.kick_ratio = 1.05 + (self.speed - 100) / 1000

    def set_speed(self, step: int):
        """
        Метод изменяет скорость лопаток.
        :param step: шаг изменения скорости "+" — вверх "-" — вниз
        """
        self.speed += step
        self.speed = min(self.speed, PADDLE_SPEED_RANGE[1])
        self.speed = max(self.speed, PADDLE_SPEED_RANGE[0])
        self.set_kick_ratio()
