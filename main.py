nodes = dict()
with open("node_coords.txt", mode="r") as file:
    for line in file:
        values = line.split(",")
        nodes[int(values[0])] = { "nx": float(values[1]), "ny": float(values[2]) }


elems = dict()
elem_num = 0
with open("elem_nodes.txt", mode="r") as file:
    while True:
        num_nodes_per_elem = file.readline()
        if num_nodes_per_elem == "":
            break
        elem_num += 1
        elem_nodes = list()
        for i in range(int(num_nodes_per_elem)):
            node = file.readline()
            elem_nodes.append(int(node))
        elems[elem_num] = { "nodes": elem_nodes }


with open("elem_shpars.txt", mode="r") as file:
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