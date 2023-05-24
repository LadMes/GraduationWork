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


def process_dimension(dimension: str):

    dimension = dimension.upper()
    if dimension == "2D" or dimension == "3D":
        return dimension
    
    raise Exception("Wrong dimension")