from layers.all_layers import average, nightmare, simple
from layers.start import start
from layers.stop import stop

layers = {
    'Тренировка': simple,
    'Игра': average,
    'NIGHTMARE': nightmare
}


def main():
    result = start()
    if result:
        score = layers[result]()
        if score:
            stop(score)


if __name__ == '__main__':
    main()
