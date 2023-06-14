import math

def process_dimension(dimension: str):

    dimension = dimension.upper()
    if dimension == "2D" or dimension == "3D":
        return dimension
    
    raise Exception("Wrong dimension")


def max_coord(nodes, coord):

    max = nodes[1]["coords"][coord]
    for node in nodes:
        if nodes[node]["coords"][coord] > max:
            max = nodes[node]["coords"][coord]
    return max


def min_coord(nodes, coord):

    min = nodes[1]["coords"][coord]
    for node in nodes:
        if nodes[node]["coords"][coord] < min:
            min = nodes[node]["coords"][coord]
    return min


def get_step(min_coord, max_coord, num_of_tiles):

    return (abs(min_coord) + abs(max_coord)) / num_of_tiles


def get_x_index(min_x, x, x_step):

    index = math.ceil((abs(min_x) + x) / x_step) - 1
    return index if index >= 0 else 0


def get_y_index(max_y, y, y_step):

    index = math.ceil((abs(max_y) - y) / y_step) - 1
    return index if index >= 0 else 0


def get_z_index(max_z, z, z_step):

    index = math.ceil((abs(max_z) - z) / z_step) - 1
    return index if index >= 0 else 0


def format_result(grid, num_of_tiles, dimension):

    if dimension == "2D":
        return format_2d_result(grid, num_of_tiles)
    else:
        return format_3d_result(grid, num_of_tiles)


def format_2d_result(grid, num_of_tiles):

    table = ""
    for i in range(num_of_tiles["num_y_tiles"]):
        row = "| "
        for j in range(num_of_tiles["num_x_tiles"]):
            row += "{:.2f}".format(grid[i][j]).zfill(5) + "% "
        table += row + "|\n"
    
    return table


def format_3d_result(grid, num_of_tiles):

    table = ""
    for k in range(num_of_tiles["num_z_tiles"]):
        table += format_2d_result(grid[k], num_of_tiles) + "\n"
        
    return table


def write_result_to_file(folder, result):

    folder = format_folder(folder)
    with open(f"{folder}result.txt", mode="w") as file:
        file.write(result)


def format_folder(folder):

    return folder if folder[-1] == "/" else folder + "/"