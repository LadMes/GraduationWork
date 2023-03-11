import numpy

from helpers import *
from elem_quality import is_bad_elem

class Grid:

    num_x_tiles = 0
    num_y_tiles = 0
    grid = []
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    def __init__(self, nodes, elems):
        self.num_x_tiles = get_num_x_tiles()
        self.num_y_tiles = get_num_y_tiles()
        self.init_grid()
        self.get_coords(nodes)
        self.populate_grid(elems)


    def init_grid(self):
        self.grid = [[ {"elems": list(), "bad_elems": list()} for _ in range(self.num_x_tiles)] for _ in range(self.num_y_tiles)]


    def get_coords(self, nodes):
        self.min_x = min_coord(nodes, "x")
        self.max_x = max_coord(nodes, "x")
        self.min_y = min_coord(nodes, "y")
        self.max_y = max_coord(nodes, "y")


    def populate_grid(self, elems):
        x_step = get_step(self.min_x, self.max_x, self.num_x_tiles)
        y_step = get_step(self.min_y, self.max_y, self.num_y_tiles)

        for i in range(1, max(elems)):
            coords = elems[i]["centroid_coords"]
            y = get_y_index(self.max_y, coords["y"], y_step)
            x = get_x_index(self.min_x, coords["x"], x_step)

            self.grid[y][x]["elems"].append(elems[i])
            if is_bad_elem(elems[i]):
                self.grid[y][x]["bad_elems"].append(elems[i])


    def calculate_percentage_bad_elems(self):
        percentage_bad_elems = numpy.zeros((self.num_y_tiles, self.num_x_tiles))

        for i in range(self.num_y_tiles):
            for j in range(self.num_x_tiles):
                num_elems = len(self.grid[i][j]["elems"])
                if num_elems != 0:
                    percentage_bad_elems[i][j] = len(self.grid[i][j]["bad_elems"]) / num_elems * 100
        
        return percentage_bad_elems