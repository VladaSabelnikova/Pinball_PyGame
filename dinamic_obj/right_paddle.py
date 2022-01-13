from typing import Union, Tuple

import pygame

from dinamic_obj.paddle_global import PaddleGlobal


class RightPaddle(PaddleGlobal):
    """
    Класс для создания правой части доски, общий для всех правых частей.
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

        self.step_angle = -3

    def update(self, *args: Tuple) -> None:
        """
        Метод изменяет изображение (берёт соответствующее из self.frames),
        создаёт новую маску и меняет силу отскока мяча от лопатки
        в зависимости от прошедшего времени и скорости.
        """
        *_, t = args[:5]
        prev_frame = int(self.cur_frame)
        if self.rotate_up:
            self.cur_frame += self.speed * t
            self.cur_frame = min(self.cur_frame, len(self.frames) - 1)

        else:
            self.cur_frame -= self.speed * t
            self.cur_frame = max(self.cur_frame, 0)

        if prev_frame != int(self.cur_frame):
            self.angle = self.start_angle + int(self.cur_frame) * \
                         self.step_angle
            self.image = self.frames[int(self.cur_frame)]
            self.mask = pygame.mask.from_surface(self.image)

        if int(self.cur_frame) in (len(self.frames) - 1, 0):
            self.rebound_ratio = self.static_rebound_ratio
        else:
            self.rebound_ratio = self.kick_ratio
