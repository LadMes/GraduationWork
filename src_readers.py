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
        fieldnames = list(map(lambda key: key.strip(), file.readline().split(',')))
        reader = csv.DictReader(file, fieldnames=fieldnames)

        keys = list(filter(lambda key: key != "id", fieldnames))
        for row in reader:
            receiver[int(row["id"])] = { "coords": dict() } 
            for key in keys:
                receiver[int(row["id"])]["coords"][key] = float(row[key])


def get_elems_shape_parameters(elems, source_folder):

    with open(f"{source_folder}/elem_shpars.txt", mode="r") as file:
        fieldnames = list(map(lambda key: key.strip(), file.readline().split(',')))
        reader = csv.DictReader(file, fieldnames)

        keys = list(filter(lambda key: key != "id", fieldnames))
        for row in reader:
            elems[int(row["id"])]["elem_shape_prop"] = dict()
            for key in keys:
                elems[int(row["id"])]["elem_shape_prop"][key] = float(row[key])


def get_num_of_tiles(source_folder):

    with open(f"{source_folder}/num_of_tiles.txt", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            return {
                "num_x_tiles": int(row["x"]),
                "num_y_tiles": int(row["y"]),
                "num_z_tiles": int(row["z"]) if "z" in row else 0
            }