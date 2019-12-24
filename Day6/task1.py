class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)


def build_orbit(node, object_dictionary):
    if node.name not in object_dictionary.keys():
        return node

    for child in object_dictionary[node.name]:
        node.add_child(build_orbit(Node(child), object_dictionary))

    return node


def print_orbit(node, depth):
    print('-' * depth + node.name)
    for child_node in node.children:
        print_orbit(child_node, depth + 1)


def orbit_count(node, depth=0):
    if not node.children:
        return depth

    total = 0
    for child in node.children:
        total += orbit_count(child, depth + 1)

    return depth + total


def build_input():
    dictionary = {}
    with open("input.txt") as inputFile:
        for line in inputFile:
            orbit = line.split(')')
            a = orbit[0].rstrip()
            b = orbit[1].rstrip()
            if a in dictionary.keys():
                dictionary[a].append(b)
            else:
                dictionary[a] = [b]
    return dictionary


def main():
    orbits = build_orbit(Node('COM'), build_input())
    # print_orbit(orbits, 0)
    print(orbit_count(orbits))


if __name__ == '__main__':

    main()
