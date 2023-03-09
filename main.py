import numpy

from src_readers import get_node_coords, get_elems
from helpers import *
from elem_quality import is_bad_elem

nodes = get_node_coords()
elems = get_elems()


min_x = min_coord(nodes, "x")
max_x = max_coord(nodes, "x")
min_y = min_coord(nodes, "y")
max_y = max_coord(nodes, "y")

num_x_tiles = get_num_x_tiles()
num_y_tiles = get_num_y_tiles()

x_step = get_step(min_x, max_x, num_x_tiles)
y_step = get_step(min_y, max_y, num_y_tiles)

grid = [[ {"elems": list(), "bad_elems": list()} for _ in range(num_x_tiles)] for _ in range(num_y_tiles)] 


for i in range(1, max(elems)):
    coords = elems[i]["centroid_coords"]
    y = get_y_index(max_y, coords["y"], y_step)
    x = get_x_index(min_x, coords["x"], x_step)

    grid[y][x]["elems"].append(elems[i])
    if is_bad_elem(elems[i]):
        grid[y][x]["bad_elems"].append(elems[i])

bad_elem_per_tile = numpy.zeros((num_y_tiles, num_x_tiles))
for i in range(num_y_tiles):
    for j in range(num_x_tiles):
        num_elems = len(grid[i][j]["elems"])
        if num_elems != 0:
            bad_elem_per_tile[i][j] = len(grid[i][j]["bad_elems"]) / num_elems * 100

print(bad_elem_per_tile)