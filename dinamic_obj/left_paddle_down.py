from typing import Union

import pygame


class LeftPaddleDown(pygame.sprite.Sprite):
    """
    Класс для создания левой нижней части доски.
    """

    def __init__(
        self,
        angle: int,
        rebound_ratio: Union[int, float],
        img: pygame.image,
        paddles: pygame.sprite.Group,
        name: str,
        columns: int,
        rows: int,
        x: int = 0,
        y: int = 0,
    ) -> None:
        super().__init__(paddles)
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
        # self.rotate_up = False

        self.step_angle = 15
        self.max_angle = self.step_angle * len(self.frames) + self.start_angle

    def cut_sheet(self, sheet: pygame.image, columns: int = 3, rows: int = 1) -> None:
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, index_frame, *args):
        self.cur_frame = index_frame
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
