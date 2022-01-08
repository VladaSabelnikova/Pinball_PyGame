from layers.all_layers import average, nightmare, simple
from layers.start import start


layers = {
    'Тренировка': simple,
    'Игра': average,
    'NIGHTMARE': nightmare
}


def main():
    result = start()
    if result:
        layers[result]()


if __name__ == '__main__':
    main()
