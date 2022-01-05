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
        kick_ratio: float,
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
            kick_ratio,
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

    def update(self, *args: Tuple) -> None:
        *_, t = args[:3]
        prev_frame = int(self.cur_frame)
        if self.rotate_up:
            self.cur_frame += self.speed * t
            self.cur_frame = min(self.cur_frame, len(self.frames) - 1)

        else:
            self.cur_frame -= self.speed * t
            self.cur_frame = max(self.cur_frame, 0)

        if prev_frame != int(self.cur_frame):
            self.angle = self.start_angle + self.cur_frame * self.step_angle
            self.image = self.frames[int(self.cur_frame)]
            self.mask = pygame.mask.from_surface(self.image)

        if self.rotate_up:
            if int(self.cur_frame) != len(self.frames) - 1:
                self.current_kick_ratio = self.kick_ratio + self.cur_frame
                print(f'{self.current_kick_ratio} = {self.kick_ratio} * {self.cur_frame}')
        else:
            self.current_kick_ratio = 1
            # print(self.current_kick_ratio)
