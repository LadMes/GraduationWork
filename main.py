import numpy

from src_readers import get_node_coords, get_elems
from helpers import *
from elem_quality import *

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

matrix = numpy.zeros((num_y_tiles, num_x_tiles))

for i in range(1, max(elems)):
    coords = elems[i]["centroid_coords"]
    matrix[get_y_index(max_y, coords["y"], y_step)][get_x_index(min_x, coords["x"], x_step)] += 1

print(matrix)