def get_node_coords():
    nodes = dict()
    with open("src/node_coords.txt", mode="r") as file:
        for line in file:
            values = line.split(",")
            nodes[int(values[0])] = { "x": float(values[1]), "y": float(values[2]) }

    return nodes


def get_elems():
    elems = get_elem_nodes()
    get_elem_centroid_coords(elems)
    get_elems_shape_parameters(elems)

    return elems


def get_elem_nodes():
    elems = dict()
    with open("src/elem_nodes.txt", mode="r") as file:
        elem_num = 0
        while True:
            try:
                num_nodes_per_elem = int(file.readline())
                elem_num += 1
                elem_nodes = list()
                for _ in range(int(num_nodes_per_elem)):
                    node = file.readline()
                    elem_nodes.append(int(node))
                elems[elem_num] = { "nodes": elem_nodes }
            except:
                break
    
    return elems


def get_elem_centroid_coords(elems):
    with open("src/elem_centroid_coords.txt", mode="r") as file:
        for line in file:
            values = line.split(",")
            elems[int(values[0])]["centroid_coords"] = { "x": float(values[1]), "y": float(values[2]) }


def get_elems_shape_parameters(elems):
    with open("src/elem_shpars.txt", mode="r") as file:
        for line in file:
            values = line.split(",")
            elems[int(values[0])]["elem_shape_prop"] = { 
                "ASPE": float(values[1]), 
                "JACR": float(values[2]), 
                "MAXA": float(values[3]), 
                "PARA": float(values[4])
            }
            if len(values) == 6:
                elems[int(values[0])]["elem_shape_prop"]["WARP"] = float(values[5])