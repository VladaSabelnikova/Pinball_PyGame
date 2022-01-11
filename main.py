from layers.all_layers import average, nightmare, simple
from layers.start import start
from layers.stop import stop
from utils.settings import ID_LAYERS

layers = [simple, average, nightmare]


def main():
    while True:
        # name_layer — выбор пользователя о том, какой уровень ему хочется.
        name_layer = start()
        if name_layer:  # Если не закрыл окно
            layer_id = ID_LAYERS[name_layer]
            layer = layers[layer_id]

            # score — кол-во набранных очков в уровне
            score = layer()
            if score:  # Если не закрыл окно
                user_choice = stop(score, layer_id)

                # user_choice — выбор пользователя о том,
                # продолжаем ли мы играть или же выходим из игры.
                if user_choice:
                    if user_choice == 'Закончить':
                        break
                else:
                    break
        else:
            break


if __name__ == '__main__':
    main()
