def decode(layer_values, width, height):
    layer_size = width * height
    decoded_layer = [''] * layer_size

    for lay_count in range(int(len(layer_values) / layer_size)):
        start_index = lay_count * layer_size
        current_layer = layer_values[start_index: start_index + layer_size]
        for index, value in enumerate(current_layer):
            if decoded_layer[index] != '' or value == '2':
                continue

            decoded_layer[index] = ' ' if value == '0' else value

    for row_count in range(height):
        start_index = row_count * width
        print (''.join(decoded_layer[start_index: start_index + width]))


def main():
    with open('input.txt') as inputFile:
        layer_values = list(inputFile.readline().rstrip('\n'))

    decode(layer_values, 25, 6)


if __name__ == '__main__':
    main()
