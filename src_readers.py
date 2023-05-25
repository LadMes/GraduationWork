import csv

def get_nodes(source_folder):

    nodes = dict()
    get_coords(f"{source_folder}/node_coords.txt", nodes)

    return nodes


def get_elems(source_folder):

    elems = dict()
    get_coords(f"{source_folder}/elem_centroid_coords.txt", elems)
    get_elems_shape_parameters(elems, source_folder)

    return elems


def get_coords(source, receiver):

    with open(source, mode="r") as file:
        for line in file:
            values = line.split(",")
            receiver[int(values[0])] = { "coords": dict() }
            receiver[int(values[0])]["coords"]["x"] = float(values[1])
            receiver[int(values[0])]["coords"]["y"] = float(values[2])
            if len(values) == 4:
                receiver[int(values[0])]["coords"]["z"] = float(values[3])


def get_elems_shape_parameters(elems, source_folder):

    shape_parameters = ["ASPE", "JACR", "MAXA", "PARA", "WARP"]
    with open(f"{source_folder}/elem_shpars.txt", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            elems[int(row["id"])]["elem_shape_prop"] = dict()
            for param in shape_parameters:
                if param in row:
                    elems[int(row["id"])]["elem_shape_prop"][param] = float(row[param])


def get_num_of_tiles(source_folder):

    with open(f"{source_folder}/num_of_tiles.txt", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            return {
                "num_x_tiles": int(row["x"]),
                "num_y_tiles": int(row["y"]),
                "num_z_tiles": int(row["z"]) if "z" in row else 0
            }