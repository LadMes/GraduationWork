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