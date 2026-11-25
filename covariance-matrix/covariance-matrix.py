import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X_arr = np.asarray(X, dtype=float)
    n = X_arr.shape[0]
    X_centered = X_arr - np.mean(X_arr, axis = 0)
    cov_matrix = (X_centered.T @ X_centered) / (n - 1)
    return cov_matrix
    pass