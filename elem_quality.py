def is_bad_elem(elem):
    return is_bad_elem_by_ASPE(elem) or is_bad_elem_by_JACR(elem) or is_bad_elem_by_MAXA(elem) or is_bad_elem_by_PARA(elem) or is_bad_elem_by_WARP(elem)


def is_bad_elem_by_ASPE(elem):

    if elem["elem_shape_prop"]["ASPE"] >= 1 and elem["elem_shape_prop"]["ASPE"] <= 5:
        return False
    
    return True


def is_bad_elem_by_JACR(elem):

    if elem["elem_shape_prop"]["JACR"] >= 1 and elem["elem_shape_prop"]["JACR"] <= 10:
        return False
    
    return True


def is_bad_elem_by_MAXA(elem):

    if elem["elem_shape_prop"]["MAXA"] >= 90 and elem["elem_shape_prop"]["MAXA"] <= 135:
        return False
    
    return True


def is_bad_elem_by_PARA(elem):

    if elem["elem_shape_prop"]["PARA"] >= 0 and elem["elem_shape_prop"]["PARA"] <= 50:
        return False
    
    return True


def is_bad_elem_by_WARP(elem):
    if "WARP" in elem["elem_shape_prop"]:
        if elem["elem_shape_prop"]["WARP"] >= 0 and elem["elem_shape_prop"]["WARP"] <= 1:
            return False
        
        return True
    
    return False