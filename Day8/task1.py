def image_size(width, height):
    return width * height


def calculate(layer_values, layer_size):
    layer_with_least_zeros = None
    for lay_count in range(int(len(layer_values) / layer_size)):
        index = lay_count * layer_size
        current_layer = layer_values[index: index + layer_size]

        if layer_with_least_zeros is None:
            layer_with_least_zeros = current_layer

        if current_layer.count('0') < layer_with_least_zeros.count('0'):
            layer_with_least_zeros = current_layer

    return layer_with_least_zeros.count('1') * layer_with_least_zeros.count('2')


def main():
    with open('input.txt') as inputFile:
        values = list(inputFile.readline().rstrip('\n'))

    print (calculate(values, image_size(25, 6)))


if __name__ == '__main__':
    main()