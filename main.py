import configparser

from src_readers import get_entity, get_elems_shape_parameters, get_num_of_tiles
from grid import *
from helpers import print_grid


config = configparser.ConfigParser()
config.read("settings.ini")

source_folder = config["common"]["source_folder"]
source_folder = source_folder if source_folder[-1] == "/" else source_folder + "/"

node_coords_file = config["file_names"]["node_coords"]
elem_centroid_coords_file = config["file_names"]["elem_centroid_coords"]
elem_shpars_file = config["file_names"]["elem_shpars"]

nodes = get_entity(source_folder + node_coords_file)
elems = get_entity(source_folder + elem_centroid_coords_file)
get_elems_shape_parameters(elems, source_folder + elem_shpars_file)

num_of_tiles = get_num_of_tiles(config["num_of_tiles"])
dimension = config["common"]["dimension"]

grid = Grid(nodes, elems, num_of_tiles, dimension)

percentage_of_bad_elems = grid.calculate_percentage_of_bad_elems()

print_grid(percentage_of_bad_elems, num_of_tiles, dimension)