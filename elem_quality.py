def is_bad_elem_by_ASPE(elem):

    if elem["elem_shape_prop"]["ASPE"] >= 1 and elem["elem_shape_prop"]["ASPE"] <= 5:
        return False
    
    return True


def is_bad_elem_by_JACR(elem):

    if elem["elem_shape_prop"]["JACR"] >= 1 and elem["elem_shape_prop"]["JACR"] <= 10:
        return False
    
    return True