class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent

    def add_child(self, node):
        self.children.append(node)

    def get_path(self):
        path = []

        node = self.parent
        while node is not None:
            path.append(node.name)
            node = node.parent

        return path

    def path_to(self, target, path=None):
        if path is None:
            path = []

        path.append(self.name)

        if self.name == target:
            return path

        if not self.children:
            return None

        for child in self.children:
            if child in path:
                continue

            possible_path = child.path_to(target, path)

            if possible_path is not None:
                return possible_path

        return None


def build_orbit(node, object_dictionary):
    if node.name not in object_dictionary.keys():
        return node

    for child in object_dictionary[node.name]:
        node.add_child(build_orbit(Node(child, node), object_dictionary))

    return node


def get_node(target, current_node):
    if current_node.name == target:
        return current_node

    if current_node.children is None:
        return None

    for child in current_node.children:
        result = get_node(target, child)
        if result is not None:
            return result

    return None


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
    print_orbit(orbits, 0)

    you_path = (get_node('YOU', orbits).get_path())
    san_path = (get_node('SAN', orbits).get_path())

    first_common_planet = None
    for planet in you_path:
        if planet in san_path:
            first_common_planet = planet
            break

    you_length = you_path.index(first_common_planet)
    san_length = san_path.index(first_common_planet)

    print(you_length + san_length)


if __name__ == '__main__':

    main()
