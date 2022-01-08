import pygame
import pygame_gui


def stop(result):

    size = (500, 660)
    pygame.init()

    pygame.display.set_caption('Конец игры')
    window_surface = pygame.display.set_mode(size)
    background = pygame.Surface(size)

    background.fill(pygame.Color((40, 40, 40)))
    manager = pygame_gui.UIManager(size)

    f1 = pygame.font.Font(None, 36)
    text = f1.render(f'Ваш результат: {result}', True, (100, 100, 100))
    place = text.get_rect(center=(250, 240))

    anew = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((60, 560), (180, 60)),
        text='Заново',
        manager=manager
    )

    close = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((270, 560), (180, 60)),
        text='Закончить',
        manager=manager
    )


    clock = pygame.time.Clock()
    while True:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    return event.ui_element.text
            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        window_surface.blit(text, place)
        manager.draw_ui(window_surface)
        pygame.display.update()


def main():
    stop(7)


if __name__ == '__main__':
    main()
