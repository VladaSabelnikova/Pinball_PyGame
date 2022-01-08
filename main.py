from layers.all_layers import average, nightmare, simple
from layers.start import start
from layers.stop import stop

layers = {
    'Тренировка': simple,
    'Игра': average,
    'NIGHTMARE': nightmare
}


def main():
    while True:
        result = start()
        if result:
            score = layers[result]()
            if score:
                user_choice = stop(score)
                if user_choice:
                    if user_choice == 'Закончить':
                        break
                else:
                    break
        else:
            break


if __name__ == '__main__':
    main()
