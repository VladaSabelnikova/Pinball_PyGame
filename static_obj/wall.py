from typing import Union

import pygame

from utils.lib import load_image


class Wall(pygame.sprite.Sprite):
    """
    Класс для создания стены.
    """

    def __init__(
        self,
        angle: int,
        rebound_ratio: Union[int, float],
        img: str,
        all_sprites: pygame.sprite.Group,
        walls: pygame.sprite.Group,
        name: str,
        x: int = 0,
        y: int = 0,
    ) -> None:
        super().__init__(all_sprites)
        self.add(walls)
        self.name = name

        self.angle = angle
        self.rebound_ratio = rebound_ratio

        self.rebound_sound = pygame.mixer.Sound('src/sounds/rebound_1.mp3')

        self.image = load_image(img)
        if self.image:
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

            self.rect.x = x
            self.rect.y = y
