import sys
from src_readers import get_nodes, get_elems, get_num_of_tiles
from grid import *
from helpers import print_grid


source_folder = sys.argv[1]

nodes = get_nodes(source_folder)
elems = get_elems(source_folder)
num_of_tiles = get_num_of_tiles(source_folder)
dimension = "3D" if num_of_tiles["num_z_tiles"] != 0 else "2D"

grid = Grid(nodes, elems, num_of_tiles, dimension=dimension)

percentage_of_bad_elems = grid.calculate_percentage_of_bad_elems()

print_grid(percentage_of_bad_elems, num_of_tiles)