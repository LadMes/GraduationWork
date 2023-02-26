nodes = dict()
with open("node_coords.txt", mode="r") as file:
    for line in file:
        values = line.split(",")
        nodes[int(values[0])] = { "nx": float(values[1]), "ny": float(values[2]) }
