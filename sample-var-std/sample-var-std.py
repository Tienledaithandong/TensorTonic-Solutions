import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    arr = np.asarray(x, dtype = float)
    centered = arr - np.mean(arr)
    var = float(np.sum(centered**2) / (arr.size-1))
    std = float(np.sqrt(var))
    return {"variance": var, "standard_deviation": std}
    pass