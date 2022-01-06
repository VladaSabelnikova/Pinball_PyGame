from typing import Tuple

import pygame


class Shadow(pygame.sprite.Sprite):
    """
    Класс для создания тени от мячика.
    """

    def __init__(
        self,
        all_sprites: pygame.sprite.Group,
        shadow: pygame.sprite.Group,
        x: int,
        y: int
    ) -> None:
        super().__init__(all_sprites)
        self.add(shadow)
        self.coeff_fading = 0.970
        self.alpha = 255
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
        self.image.set_alpha(self.alpha)
        pygame.draw.circle(
            self.image,
            pygame.Color(0, 162, 255),
            (8, 8),
            8
        )
        self.rect = self.image.get_rect()

        self.rect.x = x + 12
        self.rect.y = y + 12

    def update(self, *args: Tuple) -> None:
        """
        Задаём новое значение альфа канала и в случае,
        если оно стало меньше порогового — удаляем тень из группы.
        """
        self.alpha *= self.coeff_fading
        if self.alpha < 1:
            self.kill()
        self.image.set_alpha(self.alpha)
