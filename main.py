import configparser

from src_readers import SourceReader
from grid import Grid
from helpers import format_result, write_result_to_file


config = configparser.ConfigParser()
config.read("settings.ini")

grid_params = SourceReader(config).get_grid_params()

grid = Grid(grid_params["nodes"], 
            grid_params["elems"], 
            grid_params["num_of_tiles"], 
            grid_params["dimension"],
            grid_params["criteria_ranges"])

percentage_of_bad_elems = grid.calculate_percentage_of_bad_elems()

formatted_result = format_result(percentage_of_bad_elems, 
                                grid_params["num_of_tiles"], 
                                grid_params["dimension"])

write_result_to_file(config["common"]["source_folder"], formatted_result)