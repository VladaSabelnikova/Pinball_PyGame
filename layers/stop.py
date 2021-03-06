from typing import Union

import pygame
import pygame_gui

from utils.lib import put_results, get_results
from utils.settings import NOT_SHAMEFUL


def stop(
    score: int,
    layer_id: int
) -> Union[str, None]:
    """
    Функция возвращает вердикт по игре,
    сохраняет результаты и даёт возможность продолжить, или закончить.

    :param score: кол-во набранных баллов
    :param layer_id: id уровня, на котором играл пользователь
    :return:
    """

    fail_sound = pygame.mixer.Sound('src/sounds/fail.mp3')
    victory_sound = pygame.mixer.Sound('src/sounds/victory.mp3')
    victory_sound.set_volume(.8)

    green = (169, 220, 118)
    red = (255, 97, 136)
    default_color = (100, 100, 100)
    blue = (87, 206, 227)
    color = default_color

    current_result_font = pygame.font.Font(None, 36)
    current_record_font = pygame.font.Font(None, 26)
    cur_record_message = None

    conclusions = 'Баллы будут в режиме "Игра"'

    if layer_id > 0:
        # В противном случае это режим "Тренировка".
        # За него баллов не начисляется.
        current_record = get_results(layer_id)  # текущий рекорд по уровню.

        if current_record < int(score):  # Если побили рекорд.
            victory_sound.play()
            conclusions = f'Новый рекорд {score} баллов!'
            color = green
            put_results(score, layer_id)

        elif NOT_SHAMEFUL >= int(score):  # Если меньше порога баллов.
            fail_sound.play()
            conclusions = 'Вы проиграли: 0 баллов'
            color = red
            cur_record_message = current_record_font.render(
                f'Рекорд: {current_record}',
                True,
                blue
            )
        else:  # Иначе просто баллы, без проигрыша и рекордов.
            conclusions = f'Ваш результат: {score} баллов'
            color = blue
            cur_record_message = current_record_font.render(
                f'Рекорд: {current_record}',
                True,
                blue
            )

    text = current_result_font.render(conclusions, True, color)

    size = (500, 660)
    pygame.init()

    pygame.display.set_caption('Конец игры')
    window_surface = pygame.display.set_mode(size)
    background = pygame.Surface(size)

    background.fill(pygame.Color((40, 40, 40)))
    manager = pygame_gui.UIManager(size)
    place = text.get_rect(center=(250, 240))

    pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((60, 560), (180, 60)),
        text='Заново',
        manager=manager
    )

    pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((270, 560), (180, 60)),
        text='Закончить',
        manager=manager
    )

    clock = pygame.time.Clock()
    window_surface.blit(background, (0, 0))
    window_surface.blit(text, place)
    if cur_record_message:
        place_message_cur_record = cur_record_message.get_rect(
            center=(250, 300)
        )
        window_surface.blit(cur_record_message, place_message_cur_record)

    while True:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                victory_sound.stop()
                fail_sound.stop()
                return None

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    victory_sound.stop()
                    fail_sound.stop()
                    return event.ui_element.text  # Выбор пользователя
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(window_surface)
        pygame.display.update()


def main():
    pass


if __name__ == '__main__':
    main()
