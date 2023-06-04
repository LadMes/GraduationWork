import csv


class SourceReader:

    def __init__(self, config):
        
        self.config = config


    def get_grid_params(self):

        source_folder = self.config["common"]["source_folder"]
        source_folder = source_folder if source_folder[-1] == "/" else source_folder + "/"

        node_coords_file = self.config["file_names"]["node_coords"]
        elem_centroid_coords_file = self.config["file_names"]["elem_centroid_coords"]
        elem_shpars_file = self.config["file_names"]["elem_shpars"]

        nodes = get_entity(source_folder + node_coords_file)
        elems = get_entity(source_folder + elem_centroid_coords_file)
        get_elems_shape_parameters(elems, source_folder + elem_shpars_file)

        num_of_tiles = get_num_of_tiles(self.config["num_of_tiles"])
        dimension = self.config["common"]["dimension"]

        criteria_ranges = get_criteria_ranges(self.config, elems[1]["elem_shape_prop"].keys())

        return {
            "nodes": nodes,
            "elems": elems,
            "num_of_tiles": num_of_tiles,
            "dimension": dimension,
            "criteria_ranges": criteria_ranges
        }


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


def get_criteria_ranges(config, criteria):

    criteria_ranges = {}
    for criterion in criteria:
        criteria_ranges[criterion] = {}
        criteria_ranges[criterion]["lower_bound"] = float(config[criterion]["lower_bound"])
        criteria_ranges[criterion]["upper_bound"] = float(config[criterion]["upper_bound"])

    return criteria_ranges