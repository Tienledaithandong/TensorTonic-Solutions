import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    arr = np.asarray(A)
    n, m = arr.shape
    res = np.empty((m, n), dtype = arr.dtype)
    for i in range(n):
        for j in range(m):
            res[j, i] = arr[i, j]
    return res
    pass
