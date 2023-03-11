from src_readers import get_node_coords, get_elems
from grid import *


nodes = get_node_coords()
elems = get_elems()

grid = Grid(nodes)
grid.populate_grid(elems)

percentage_bad_elems = grid.calculate_percentage_bad_elems()

print(percentage_bad_elems)