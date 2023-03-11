from src_readers import get_node_coords, get_elems
from grid import *


nodes = get_node_coords()
elems = get_elems()

grid = Grid(nodes, elems)

percentage_bad_elems = GridUtilities.calculate_percentage_bad_elems(grid)

print(percentage_bad_elems)