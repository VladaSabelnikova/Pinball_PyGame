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

        self.angle_down = angle
        self.angle = angle
        self.rebound_ratio = rebound_ratio

        self.frames = []
        self.cut_sheet(img, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def cut_sheet(self, sheet, columns=3, rows=1):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, is_rotate=False):
        # coeff_angle = 3 if is_rotate else -3
        # self.angle += coeff_angle
        # if self.angle < self.angle_down:
        #     self.angle = self.angle_down
        # elif self.angle > self.angle_down + 90:
        #     self.angle = self.angle_down + 90

        if is_rotate:
            self.cur_frame = min(self.cur_frame + 1, len(self.frames) - 1)
        else:
            self.cur_frame = max(self.cur_frame - 1, 0)

        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
