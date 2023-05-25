from src_readers import get_nodes, get_elems, get_num_of_tiles
from grid import *

source_folder = "src/3D"

nodes = get_nodes(source_folder)
elems = get_elems(source_folder)
num_of_tiles = get_num_of_tiles(source_folder)


grid = Grid(nodes, elems, num_of_tiles, dimension="3D")

percentage_of_bad_elems = grid.calculate_percentage_of_bad_elems()

print(percentage_of_bad_elems)