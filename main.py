from src_readers import get_nodes, get_elems
from grid import *


nodes = get_nodes("src/2D")
elems = get_elems("src/2D")

grid = Grid(nodes, elems)

percentage_of_bad_elems = grid.calculate_percentage_of_bad_elems()

print(percentage_of_bad_elems)