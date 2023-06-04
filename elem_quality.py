def is_bad_elem(elem, criteria_ranges):

    for criterion in criteria_ranges:
        if (elem["elem_shape_prop"][criterion] < criteria_ranges[criterion]["lower_bound"]
            or elem["elem_shape_prop"][criterion] > criteria_ranges[criterion]["upper_bound"]):
            return True
    
    return False
