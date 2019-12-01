import math


def main():
    total = 0
    with open('input1.txt', 'r') as f:
        for line in f:
            total += (mass_to_fuel(int(line)))
    return total


def mass_to_fuel(mass):
    return math.floor(mass / 3) - 2


if __name__ == '__main__':
    print(main())
