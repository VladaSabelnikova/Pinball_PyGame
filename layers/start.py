from typing import Union

import pygame
import pygame_gui


def start() -> Union[str, None]:
    """
    Функция создаёт стартовое окно с выбором уровня игры.

    :return: Вернёт выбор уровня от пользователя.
    """
    size = (500, 660)
    pygame.init()

    pygame.mixer.music.load('src/sounds/start_theme.mp3')

    pygame.display.set_caption('Стартовое окно')
    window_surface = pygame.display.set_mode(size)
    background = pygame.Surface(size)

    background.fill(pygame.Color((40, 40, 40)))
    manager = pygame_gui.UIManager(size)

    simple_level = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((160, 160), (180, 60)),
        text='Тренировка',
        manager=manager
    )

    average_level = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((160, 250), (180, 60)),
        text='Игра',
        manager=manager
    )

    nightmare_level = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((160, 340), (180, 60)),
        text='NIGHTMARE',
        manager=manager
    )

    clock = pygame.time.Clock()
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    while True:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                return None

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    pygame.mixer.music.stop()
                    return event.ui_element.text  # название кнопочки
            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()


def main():
    start()


if __name__ == '__main__':
    main()
