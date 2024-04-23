import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

distance_matrix = np.array([
    [0,  6, 7, 13, 1, 3],
    [7,  0, 8,  2, 9, 7],
    [5, 10, 0, 10, 1, 7],
    [8,  6, 5,  0, 5, 1],
    [7,  7, 6,  7, 0, 4],
    [9,  8, 8,  5, 3, 0]
])
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
print(distance)
print(permutation)