import datetime
import pathlib
import random
from math import radians, sqrt, asin, acos, pi, degrees, sin, cos
from pathlib import Path
from typing import List, Union, Tuple

import pygame

from log import create_logger
from settings import LOG_LEVEL, BREAKING_POINT


def load_image(name: str, colorkey=None) -> pygame.image:
    """
    Функция вернёт surface на котором расположено изображение.
    """
    fullname = Path(f'src/{name}')
    if not fullname.is_file():  # если fullname не файл
        logger.error(f'Файл с изображением "{fullname}" не найден')
        return
    image = pygame.image.load(fullname)
    return image


def __encrypt__(*args, **kwargs):
    row_result, *_ = args
    encoded_result = [int(elem) for elem in row_result]
    step_1, step_2 = encoded_result[-2:]

    for i in range(1, len(encoded_result) - 2):
        elem = encoded_result[i]
        encoded_result[i] = (((elem + step_1) % 10) + step_2) % 10
    encoded_result = ''.join([f'{elem}' for elem in encoded_result])

    return encoded_result


def __decipher__(*args, **kwargs):
    encoded_result, *_ = args
    row_result = [int(elem) for elem in encoded_result]
    step_1, step_2 = row_result[-2:][::-1]

    for i in range(1, len(encoded_result) - 2):
        elem = row_result[i]
        row_result[i] = (((elem - step_1) % 10) - step_2) % 10
    row_result = ''.join([f'{elem}' for elem in row_result])

    return row_result


def get_reflected_vector(
    vector: List[Union[int, float]],
    wall: pygame.sprite.Sprite,
    *args: Tuple
) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Функция возвращает новое направление вектора
    в случае столкновения со стеной.
    """

    x, y = vector
    wall_angle = radians(wall.angle)

    # Длинна вектора является гипотенузой,
    # следовательно, по Т. Пифагора находим её длину.
    vector_len = sqrt(x ** 2 + y ** 2)

    # Что бы не высчитать одинаковые углы у векторов на разных четвертях —
    # нам, в зависимости от того, в какой четверти расположен вектор,
    # нужно высчитывать либо его sin, либо его cos.

    # Так как в геометрии ось Y направлена вверх,
    # а на мониторах вниз, то мы будем инвертировать Y (высоту).

    if x > 0 and y <= 0:  # если вектор направлен в 1-ю координатную четверть
        vector_sin = -y / vector_len
        vector_angle = asin(vector_sin)

    elif x <= 0 and y < 0:  # если вектор направлен в 2-ю координатную четверть
        vector_cos = x / vector_len
        vector_angle = acos(vector_cos)

    elif x < 0 and y >= 0:  # если вектор направлен в 3-ю координатную четверть
        vector_cos = x / vector_len
        vector_angle = -acos(vector_cos)
        vector_angle += pi * 2  # вычисляем размер угла из отрицательного

    elif x >= 0 and y > 0:  # если вектор направлен в 4-ю координатную четверть
        vector_sin = -y / vector_len
        vector_angle = asin(vector_sin)
        vector_angle += pi * 2  # вычисляем размер угла из отрицательного
    # print('vector_angle — ', degrees(vector_angle))

    # Есть диапазон углов, с которым вектор гарантировано не будет пересекаться
    # Нам нужно проверить, не входит ли угол поверхности в этот диапазон.
    # Если входит — возвращаем тот же самый вектор,
    # так как с этой поверхностью пересечений нет.
    not_collide_range = (vector_angle + pi) % (pi * 2)

    # Если vector_angle > pi —
    # есть часть диапазона от нуля и до not_collide_range.
    # Значит нужно проверить два условия,
    # так как в этом случае диапазон делится на две части.
    if vector_angle > pi:
        if vector_angle <= wall_angle <= pi * 2 or \
            0 <= wall_angle <= not_collide_range:
            logger.debug(
                f'\nУгол вектора      {degrees(vector_angle)}\n'
                f'Вектор отскока    {x, y}\n'
                f'Нет столкновения\n'
                f'----------------------------'
            )
            return x, y
    else:  # В противном случае диапазон один.
        if vector_angle <= wall_angle <= not_collide_range:
            logger.debug(
                f'\nУгол вектора      {degrees(vector_angle)}\n'
                f'Вектор отскока    {x, y}\n'
                f'Нет столкновения\n'
                f'----------------------------'
            )
            return x, y

    # Находим угол столкновения по Т. О сумме углов треугольника.
    # pi - wall_angle — вычитаем из pi так как находим внутренний угол.
    # В общем виде так:
    # collide_angle = сумма всех углов - сумма внутреннего угла wall_angle
    # и угла вектора vector_angle.
    collide_angle = (pi - (pi - wall_angle + vector_angle))
    new_vector_angle = collide_angle + wall_angle

    logger.debug(
        f'\nУгол вектора      {degrees(vector_angle)}\n'
        f'Угол столкновения {degrees(collide_angle)}\n'
        f'Угол отскока      {degrees(new_vector_angle)}\n'
        f'----------------------------'
    )

    new_vector_angle_sin = sin(-new_vector_angle)  # инвертируем обратно ось Y
    new_vector_angle_cos = cos(new_vector_angle)

    new_vector_len = vector_len * wall.rebound_ratio  # гасим отскок на коэффициент

    new_x = new_vector_angle_cos * new_vector_len
    new_y = new_vector_angle_sin * new_vector_len
    logger.debug(
        f'\nВектор отскока   {new_x, new_y}\n'
        f'----------------------------'
    )

    return new_x, new_y


def result_file_open():
    user_results = Path('user_results.txt')
    if not user_results.exists():
        user_results.write_text('-1\n-1\n-1')
    data = user_results.read_text('utf-8').split('\n')
    return user_results, data


def put_results(score, layer_id):
    date = ''.join(f'{datetime.date.today()}'.split('-'))
    step_1, step_2 = random.randrange(10), random.randrange(10)
    row_result = f'{layer_id}{score}{date}{step_1}{step_2}'

    encrypted_result = __encrypt__(row_result)

    # user_results = Path('user_results.txt')
    # data = user_results.read_text('utf-8').split('\n')

    user_results, data = result_file_open()

    data[int(encrypted_result[0])] = encrypted_result

    user_results.write_text('\n'.join(data))


def get_results(layer_id):
    user_results, data = result_file_open()
    result_from_id = data[layer_id]
    if result_from_id == '-1':
        return int(result_from_id)
    output = __decipher__(result_from_id)
    output = int(output[1:-10])
    return output


def result_calculation(game_time, extra_balls):
    return int(100_000 / (game_time * (3 - extra_balls)))


def get_reflected_vector_paddle(
    vector: List[Union[int, float]],
    paddle: pygame.sprite.Sprite,
    the_same: bool,
    *args: Tuple,
) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Функция возвращает новое направление вектора
    в случае столкновения с лопаткой.

    :param vector: Текущее направление вектора.
    :param w_angle: Угол поверхности,
    с которой столкнулся вектор (изначально в градусах).
    :param rebound_ratio: Сила отскока от препятствия.
    :return: Новое направление вектора.
    """

    x, y = vector
    wall_angle = radians(paddle.angle)
    follow = False

    logger.debug(
        f'\nВходящий вектор   {x, y}\n'
    )

    # Длинна вектора является гипотенузой,
    # следовательно, по Т. Пифагора находим её длину.
    vector_len = sqrt(x ** 2 + y ** 2)

    # Что бы не высчитать одинаковые углы у векторов на разных четвертях —
    # нам, в зависимости от того, в какой четверти расположен вектор,
    # нужно высчитывать либо его sin, либо его cos.

    # Так как в геометрии ось Y направлена вверх,
    # а на мониторах вниз, то мы будем инвертировать Y (высоту).

    if x > 0 and y <= 0:  # если вектор направлен в 1-ю координатную четверть
        vector_sin = -y / vector_len
        vector_angle = asin(vector_sin)

    elif x <= 0 and y < 0:  # если вектор направлен в 2-ю координатную четверть
        vector_cos = x / vector_len
        vector_angle = acos(vector_cos)

    elif x < 0 and y >= 0:  # если вектор направлен в 3-ю координатную четверть
        vector_cos = x / vector_len
        vector_angle = -acos(vector_cos)
        vector_angle += pi * 2  # вычисляем размер угла из отрицательного

    elif x >= 0 and y > 0:  # если вектор направлен в 4-ю координатную четверть
        vector_sin = -y / vector_len
        vector_angle = asin(vector_sin)
        vector_angle += pi * 2  # вычисляем размер угла из отрицательного

    # Есть диапазон углов, с которым вектор гарантировано не будет пересекаться
    # Нам нужно проверить, не входит ли угол поверхности в этот диапазон.
    # Если входит — возвращаем тот же самый вектор,
    # так как с этой поверхностью пересечений нет.
    not_collide_range = (vector_angle + pi) % (pi * 2)

    # Если vector_angle > pi —
    # есть часть диапазона от нуля и до not_collide_range.
    # Значит нужно проверить два условия,
    # так как в этом случае диапазон делится на две части.
    if vector_angle > pi:
        if vector_angle <= wall_angle <= pi * 2 or 0 <= wall_angle <= not_collide_range:
            if the_same:
                # vector_angle += pi
                follow = True
            else:
                return x, y
    else:  # В противном случае диапазон один.
        if vector_angle <= wall_angle <= not_collide_range:
            if the_same:
                # vector_angle += pi
                follow = True
            else:
                return x, y

    # Находим угол столкновения по Т. О сумме углов треугольника.
    # pi - wall_angle — вычитаем из pi так как находим внутренний угол.
    # В общем виде так:
    # collide_angle = сумма всех углов - сумма внутреннего угла wall_angle
    # и угла вектора vector_angle.
    collide_angle = (pi - (pi - wall_angle + vector_angle))
    # if the_same and follow:
    #     vector_angle -= collide_angle
    if the_same and follow:
        new_vector_angle = vector_angle
    else:
        new_vector_angle = collide_angle + wall_angle

    # if the_same and follow:
    #     print(degrees(wall_angle), degrees(new_vector_angle))
    # else:
    #     print()

    logger.debug(
        f'\nУгол вектора      {degrees(vector_angle) % 360}\n'
        f'Угол столкновения {degrees(collide_angle) % 360}\n'
        f'Угол отскока      {degrees(new_vector_angle) % 360}\n'
        f'wall_angle        {degrees(wall_angle) % 360}\n'
    )

    new_vector_angle_sin = sin(-new_vector_angle)  # инвертируем обратно ось Y
    new_vector_angle_cos = cos(new_vector_angle)

    new_vector_len = vector_len * paddle.rebound_ratio  # гасим отскок на коэффициент

    new_x = new_vector_angle_cos * new_vector_len
    new_y = new_vector_angle_sin * new_vector_len
    logger.debug(
        f'\nВектор отскока   {new_x, new_y}\n'
        f'----------------------------'
    )

    return new_x, new_y


def get_reflected_vector_blot(
    vector: List[Union[int, float]],
    blot: pygame.sprite.Sprite,
    *args: Tuple,
) -> Tuple[Union[int, float], Union[int, float]]:
    ball = args[-1]
    x, y = vector
    new_x, new_y = x, y

    if not blot.broken:
        vector_len = sqrt(x ** 2 + y ** 2)

        if vector_len >= BREAKING_POINT:
            blot.broken = True
            ball.kill()
        else:
            blot.creation_angle(ball)
            # print(blot.angle)
            new_x, new_y = get_reflected_vector(vector, blot)
            # new_x, new_y = get_reflected_vector_paddle(vector, blot, False)

    return new_x, new_y


def get_reflected_vector_bumper(
    vector: List[Union[int, float]],
    bumper: pygame.sprite.Sprite,
    *args: Tuple,
) -> Tuple[Union[int, float], Union[int, float]]:
    ball = args[-1]
    bumper.creation_angle(ball)
    new_x, new_y = get_reflected_vector(vector, bumper)
    return new_x, new_y


logger = create_logger(name=__name__, level=LOG_LEVEL)
