import math

def max_coord(nodes, coord):
    max = nodes[1]["coords"][coord]
    for node in nodes:
        if nodes[node]["coords"][coord] > max:
            max = nodes[node]["coords"][coord]
    return max


def min_coord(nodes, coord):
    min = nodes[1]["coords"][coord]
    for node in nodes:
        if nodes[node]["coords"][coord] < min:
            min = nodes[node]["coords"][coord]
    return min


def get_num_x_tiles():
    return 7


def get_num_y_tiles():
    return 5


def get_step(min_coord, max_coord, num_tiles):
    return (abs(min_coord) + abs(max_coord)) / num_tiles


def get_x_index(min_x, x, x_step):
    index = math.ceil((abs(min_x) + x) / x_step) - 1
    return index if index >= 0 else 0


def get_y_index(max_y, y, y_step):
    index = math.ceil((abs(max_y) - y) / y_step) - 1
    return index if index >= 0 else 0