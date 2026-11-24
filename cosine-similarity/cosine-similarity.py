import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    arr_a = np.array(a, dtype = float)
    arr_b = np.array(b, dtype = float)
    dot_ab = np.dot(arr_a, arr_b)
    norm_a = np.linalg.norm(arr_a)
    norm_b = np.linalg.norm(arr_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot_ab/(norm_a*norm_b))
    pass