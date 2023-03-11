from src_readers import get_node_coords, get_elems
from helpers import *
from grid import *


nodes = get_node_coords()
elems = get_elems()

grid = Grid(get_num_y_tiles(), get_num_x_tiles(), nodes)
grid.populate_grid(elems)

percentage_bad_elems = grid.calculate_percentage_bad_elems()

print(percentage_bad_elems)