from helpers import *
from elem_quality import is_bad_elem

class Grid:

    grid = []
    dimension = "2D"
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


    def __init__(self, nodes, elems, num_of_tiles, dimension):
        self.dimension = process_dimension(dimension)
        self.num_of_tiles = num_of_tiles
        self.grid = self.init_grid()
        self.init_min_max_coords(nodes)
        self.populate_grid(elems)


    def init_grid(self):

        if self.dimension == "2D":
            return self.init_2d_grid()
        else:
            return self.init_3d_grid()


    def init_2d_grid(self):

        return [[ {"elems": list(), "bad_elems": list()} 
                      for _ in range(self.num_of_tiles["num_x_tiles"])] 
                      for _ in range(self.num_of_tiles["num_y_tiles"])]


    def init_3d_grid(self):

        return [self.init_2d_grid() for _ in range(self.num_of_tiles["num_z_tiles"])]


    def init_min_max_coords(self, nodes):

        self.min_max_coords["min_x"] = min_coord(nodes, "x")
        self.min_max_coords["max_x"] = max_coord(nodes, "x")
        self.min_max_coords["min_y"] = min_coord(nodes, "y")
        self.min_max_coords["max_y"] = max_coord(nodes, "y")
        if self.dimension == "3D":
            self.min_max_coords["min_z"] = min_coord(nodes, "z")
            self.min_max_coords["max_z"] = max_coord(nodes, "z")


    def populate_grid(self, elems):

        x_step = get_step(self.min_max_coords["min_x"], 
                          self.min_max_coords["max_x"], 
                          self.num_of_tiles["num_x_tiles"])
        y_step = get_step(self.min_max_coords["min_y"], 
                          self.min_max_coords["max_y"], 
                          self.num_of_tiles["num_y_tiles"])
        
        if self.dimension == "3D":
            z_step = get_step(self.min_max_coords["min_z"], 
                              self.min_max_coords["max_z"], 
                              self.num_of_tiles["num_z_tiles"])

        for i in range(1, max(elems)):
            coords = elems[i]["coords"]
            y = get_y_index(self.min_max_coords["max_y"], coords["y"], y_step)
            x = get_x_index(self.min_max_coords["min_x"], coords["x"], x_step)
            zone = {}
            if self.dimension == "3D":
                z = get_z_index(self.min_max_coords["max_z"], coords["z"], z_step)
                zone = self.grid[z][y][x]
            else:
                zone = self.grid[y][x]

            zone["elems"].append(elems[i])
            if is_bad_elem(elems[i]):
                zone["bad_elems"].append(elems[i])


    def calculate_percentage_of_bad_elems(self):

        if self.dimension == "3D":
            return self.calculate_percentage_of_bad_elems_in_3D_grid(self.grid)
        else:
            return self.calculate_percentage_of_bad_elems_in_2D_grid(self.grid)
    

    def calculate_percentage_of_bad_elems_in_2D_grid(self, grid):

        percentage_of_bad_elems = [[ 0 for _ in range(self.num_of_tiles["num_x_tiles"])] 
                                       for _ in range(self.num_of_tiles["num_y_tiles"])]

        for i in range(self.num_of_tiles["num_y_tiles"]):
            for j in range(self.num_of_tiles["num_x_tiles"]):
                num_elems = len(grid[i][j]["elems"])
                if num_elems != 0:
                    percentage_of_bad_elems[i][j] = len(grid[i][j]["bad_elems"]) / num_elems * 100
            
        return percentage_of_bad_elems
    

    def calculate_percentage_of_bad_elems_in_3D_grid(self, grid):

        percentage_of_bad_elems = []

        for k in range(self.num_of_tiles["num_z_tiles"]):
            percentage_of_bad_elems.append(self.calculate_percentage_of_bad_elems_in_2D_grid(grid[k]))
            
        return percentage_of_bad_elems