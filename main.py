from layers.all_layers import average, nightmare, simple
from layers.start import start
from layers.stop import stop
from settings import ID_LAYERS

layers = [simple, average, nightmare]


def main():
    while True:
        name_layer = start()
        if name_layer:
            layer_id = ID_LAYERS[name_layer]
            layer = layers[layer_id]
            score = layer()
            if score:
                user_choice = stop(score, layer_id)
                if user_choice:
                    if user_choice == 'Закончить':
                        break
                else:
                    break
        else:
            break


if __name__ == '__main__':
    main()
