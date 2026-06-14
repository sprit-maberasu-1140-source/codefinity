import numpy as np
import pandas as pd

def compute_svd_recommendation(ratings_matrix, k=2):
    """
    Factorize the ratings_matrix using SVD and reconstruct an approximation using top k singular values.
    Return the reconstructed matrix.
    """
    U, S, VT = np.linalg.svd(ratings_matrix, full_matrices=False)
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    VT_k = VT[:k, :]
    approx_matrix = np.dot(U_k, np.dot(S_k, VT_k))
    return approx_matrix

# Example ratings matrix (users as rows, items as columns)
ratings_matrix = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
])

approx_matrix = compute_svd_recommendation(ratings_matrix, k=2)
