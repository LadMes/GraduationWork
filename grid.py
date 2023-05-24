import numpy

from helpers import *
from elem_quality import is_bad_elem

class Grid:

    grid = []
    num_of_tiles = {
        "num_x_tiles": 0,
        "num_y_tiles": 0,
        "num_z_tiles": 0
    }
    min_max_coords = {
        "min_x": 0,
        "max_x": 0,
        "min_y": 0,
        "max_y": 0,
        "min_z": 0,
        "max_z": 0
    }


    def __init__(self, nodes, elems, dimension="2D"):
        dimension = process_dimension(dimension)
        self.init_num_of_tiles(dimension)
        self.init_grid(dimension)
        self.init_min_max_coords(nodes, dimension)
        self.populate_grid(elems, dimension)


    def init_num_of_tiles(self, dimension):
        self.num_of_tiles["num_x_tiles"] = get_num_x_tiles()
        self.num_of_tiles["num_y_tiles"] = get_num_y_tiles()
        if dimension == "3D":
            self.num_of_tiles["num_z_tiles"] = get_num_z_tiles()


    def init_grid(self, dimension):

        if dimension == "2D":
            self.init_2d_grid()
        else:
            self.init_3d_grid()


    def init_2d_grid(self):

        self.grid = [[ {"elems": list(), "bad_elems": list()} 
                      for _ in range(self.num_of_tiles["num_x_tiles"])] 
                      for _ in range(self.num_of_tiles["num_y_tiles"])]


    def init_3d_grid(self):

        self.grid = [[[ {"elems": list(), "bad_elems": list()} 
                      for _ in range(self.num_of_tiles["num_x_tiles"])] 
                      for _ in range(self.num_of_tiles["num_y_tiles"])] 
                      for _ in range(self.num_of_tiles["num_z_tiles"])]


    def init_min_max_coords(self, nodes, dimension):

        self.min_max_coords["min_x"] = min_coord(nodes, "x")
        self.min_max_coords["max_x"] = max_coord(nodes, "x")
        self.min_max_coords["min_y"] = min_coord(nodes, "y")
        self.min_max_coords["max_y"] = max_coord(nodes, "y")
        if dimension == "3D":
            self.min_max_coords["min_z"] = min_coord(nodes, "z")
            self.min_max_coords["max_z"] = max_coord(nodes, "z")

    # TODO: Correct this
    def populate_grid(self, elems):
        x_step = get_step(self.min_x, self.max_x, self.num_x_tiles)
        y_step = get_step(self.min_y, self.max_y, self.num_y_tiles)

        for i in range(1, max(elems)):
            coords = elems[i]["coords"]
            y = get_y_index(self.max_y, coords["y"], y_step)
            x = get_x_index(self.min_x, coords["x"], x_step)

            self.grid[y][x]["elems"].append(elems[i])
            if is_bad_elem(elems[i]):
                self.grid[y][x]["bad_elems"].append(elems[i])

# TODO: Correct this
class GridUtilities:
    
    def calculate_percentage_bad_elems(grid):
        percentage_bad_elems = numpy.zeros((grid.num_y_tiles, grid.num_x_tiles))

        for i in range(grid.num_y_tiles):
            for j in range(grid.num_x_tiles):
                num_elems = len(grid.grid[i][j]["elems"])
                if num_elems != 0:
                    percentage_bad_elems[i][j] = len(grid.grid[i][j]["bad_elems"]) / num_elems * 100
            
        return percentage_bad_elems