"""
В файле лежат константы и настройки.
"""

LOG_LEVEL = 'INFO'
BALL_PATH = 'sprites/ball.png'
KEY_UP = 1073741906
KEY_DOWN = 1073741905
PADDLE_SPEED = 250
PADDLE_SPEED_RANGE = (100, 500)
BLOT_SPEED = 36
MAX_SPEED = 3000

BUMP_REBOUND_RATIO_LATERAL = 0.8
BUMP_REBOUND_RATIO_CENTER = 0.5

KEY_LEFT = 1073742048
KEY_RIGHT = 1073742052
BALL_PAUSE = 2

SIMPLE_BREAKING_POINT = 1200
AVERAGE_BREAKING_POINT = 1700
NIGHTMARE_BREAKING_POINT = 1800


SIMPLE_GRAVITY = 1600
AVERAGE_GRAVITY = 2800
NIGHTMARE_GRAVITY = 3800

EXTRA_BALLS = 2

ID_LAYERS = {
    'Тренировка': 0,
    'Игра': 1,
    'NIGHTMARE': 2
}

NOT_SHAMEFUL = -1

SOUND_GAP = .01

SOUND_VOLUME_CONTROL = 3_600_000
