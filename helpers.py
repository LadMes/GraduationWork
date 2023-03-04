import math

def max_coord(nodes, coord):
    max = nodes[1][coord]
    for node in nodes:
        if nodes[node][coord] > max:
            max = nodes[node][coord]
    return max

def min_coord(nodes, coord):
    min = nodes[1][coord]
    for node in nodes:
        if nodes[node][coord] < min:
            min = nodes[node][coord]
    return min


def get_num_x_tiles():
    return 7


def get_num_y_tiles():
    return 5


def get_step(min_coord, max_coord, num_tiles):
    return (abs(min_coord) + abs(max_coord)) / num_tiles


def get_index(min_coord, coord, step):
    index = math.ceil((abs(min_coord) + coord) / step) - 1
    return index if index >= 0 else 0