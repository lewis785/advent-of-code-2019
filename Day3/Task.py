def manhattan(point):
    return sum(map(abs, point))


def path(steps):
    x, y = 0, 0
    wire = {}
    i = 0
    for s in steps:
        d = s[0]
        count = int(s[1:])
        for _ in range(count):
            i += 1
            if d == 'U':
                y += 1
            elif d == 'D':
                y -= 1
            elif d == 'L':
                x -= 1
            elif d == 'R':
                x += 1
            wire[x, y] = i
    return wire


def main():
    with open('input.txt') as inputFile:
        wire1 = inputFile.readline().split(',')
        wire2 = inputFile.readline().split(',')

        wire1_path = path(wire1)
        wire2_path = path(wire2)

        intersections = set(wire1_path) & set(wire2_path)

        distances = {}
        for point in intersections:
            distances[manhattan(point)] = wire1_path[point] + wire2_path[point]

        print("Task 1: " + str(min(distances.keys())))
        print("Task 2: " + str(min(distances.values())))


if __name__ == '__main__':
    main()
