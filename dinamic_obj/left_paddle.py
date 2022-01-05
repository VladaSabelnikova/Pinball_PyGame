from typing import Union, Tuple

import pygame

from dinamic_obj.paddle_global import PaddleGlobal


class LeftPaddle(PaddleGlobal):
    """
    Класс для создания левой части доски, общий для всех левых частей.
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

        super().__init__(
            angle,
            rebound_ratio,
            img,
            paddles,
            all_sprites,
            name,
            columns,
            rows,
            x,
            y
        )

        self.step_angle = 3
        self.max_angle = self.step_angle * len(self.frames) + self.start_angle

    def update(self, *args: Tuple) -> None:
        *_, t = args[:3]
        if self.rotate_up:
            self.cur_frame = min(self.cur_frame + 1, len(self.frames) - 1)
            self.angle = min(self.angle + self.step_angle,
                             self.start_angle + 87)

        else:
            self.cur_frame = max(self.cur_frame - 1, 0)
            self.angle = max(self.angle - self.step_angle * t, self.start_angle)
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
