import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    arr_x = np.array(x, dtype = float)
    arr_y = np.array(y, dtype = float)
    return float(np.dot(arr_x, arr_y))
    pass