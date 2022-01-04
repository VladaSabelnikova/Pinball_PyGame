from typing import Union

import pygame


class Paddle(pygame.sprite.Sprite):
    """
    Класс для создания дощечек.
    """

    def __init__(
        self,
        angle: int,
        rebound_ratio: Union[int, float],
        img: pygame.image,
        all_sprites: pygame.sprite.Group,
        walls: pygame.sprite.Group,
        name: str,
        columns: int,
        rows: int,
        x: int = 0,
        y: int = 0,
    ) -> None:
        super().__init__(all_sprites)
        self.add(walls)
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

        self.step_angle = 15 if self.name == 'paddle_left' else -15  # заменить при большем кол-ве картинок
        self.max_angle = self.step_angle * len(self.frames) + self.start_angle

    def cut_sheet(self, sheet: pygame.image, columns: int = 3, rows: int = 1) -> None:
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args) -> None:

        if self.rotate_up:
            self.angle = min(self.angle + self.step_angle, self.max_angle)
            self.cur_frame = min(self.cur_frame + 1, len(self.frames) - 1)
        else:
            self.angle = max(self.angle - self.step_angle, self.start_angle)
            self.cur_frame = max(self.cur_frame - 1, 0)

        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
