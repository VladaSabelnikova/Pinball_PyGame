import pygame


def creation_general_settings():
    pygame.init()
    pygame.display.set_caption('Игра')
    all_sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode((500, 660))
    shadow = pygame.sprite.Group()

    paddles = pygame.sprite.Group()
    bumpers = pygame.sprite.Group()
    blots = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    return all_sprites, screen, shadow, paddles, bumpers, blots, walls
