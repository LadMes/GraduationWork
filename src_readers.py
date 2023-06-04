import csv


def get_entity(source):

    entity = dict()
    get_coords(source, entity)

    return entity


def get_coords(source, receiver):

    with open(source, mode="r") as file:
        fieldnames = list(map(lambda key: key.strip(), file.readline().split(',')))
        reader = csv.DictReader(file, fieldnames=fieldnames)

        keys = list(filter(lambda key: key != "id", fieldnames))
        for row in reader:
            receiver[int(row["id"])] = { "coords": dict() } 
            for key in keys:
                receiver[int(row["id"])]["coords"][key] = float(row[key])


def get_elems_shape_parameters(elems, source):

    with open(source, mode="r") as file:
        fieldnames = list(map(lambda key: key.strip(), file.readline().split(',')))
        reader = csv.DictReader(file, fieldnames=fieldnames)

        keys = list(filter(lambda key: key != "id", fieldnames))
        for row in reader:
            elems[int(row["id"])]["elem_shape_prop"] = dict()
            for key in keys:
                elems[int(row["id"])]["elem_shape_prop"][key] = float(row[key])


def get_num_of_tiles(source):
    return {
        "num_x_tiles": int(source["num_x_tiles"]),
        "num_y_tiles": int(source["num_y_tiles"]),
        "num_z_tiles": int(source["num_z_tiles"]) if "num_z_tiles" in source else 0
    }