from src_readers import get_nodes, get_elems
from grid import *


nodes = get_nodes()
elems = get_elems()

grid = Grid(nodes, elems)

percentage_bad_elems = GridUtilities.calculate_percentage_bad_elems(grid)

print(percentage_bad_elems)