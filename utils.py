from math import radians, sqrt, asin, acos, pi, degrees, sin, cos
from pathlib import Path
from typing import List, Union, Tuple

import pygame

from log import create_logger
from settings import LOG_LEVEL


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


def get_reflected_vector_paddle(
    vector: List[Union[int, float]],
    paddle: pygame.sprite.Sprite,
    the_same: bool
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
                vector_angle += pi
            else:
                return x, y
    else:  # В противном случае диапазон один.
        if vector_angle <= wall_angle <= not_collide_range:
            if the_same:
                vector_angle += pi
            else:
                return x, y

    # Находим угол столкновения по Т. О сумме углов треугольника.
    # pi - wall_angle — вычитаем из pi так как находим внутренний угол.
    # В общем виде так:
    # collide_angle = сумма всех углов - сумма внутреннего угла wall_angle
    # и угла вектора vector_angle.
    collide_angle = (pi - (pi - wall_angle + vector_angle))
    new_vector_angle = collide_angle + wall_angle

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


logger = create_logger(name=__name__, level=LOG_LEVEL)
