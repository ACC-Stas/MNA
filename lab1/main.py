import numpy as np
import gauss_functions as gf
from copy import deepcopy


def print_answer(deviation: list[float], output_values: list[float]) -> None:
    print("Answer:")
    for idx, item in enumerate(output_values):
        print(f"X {idx} = {item}")

    print("Error:")
    for idx, item in enumerate(deviation):
        print(f"X {idx} = {item}")

    print("Relative error:")
    for idx, item in enumerate(deviation):
        print(f"X {idx} = {item / 4.2}")


def print_matrix(matrix):
    print(np.matrix(matrix))
    print()


matrixA = [[4.7300, 0.8100, 3.0700, 0.9200, -0.5300, 4.2],
           [-0.5300, 4.7300, 0.8100, 3.0700, 0.9200, 4.2],
           [3.3200, -0.5300, 4.7300, 0.8100, 3.0700, 4.2],
           [0.6700, 3.3200, -0.5300, 4.7300, 0.8100, 4.2],
           [0.8100, 0.6700, 3.3200, -0.5300, 4.7300, 4.2]]

if __name__ == "__main__":
    print('Input matrix:')
    print_matrix(matrixA)
    triangled = gf.make_triangle_simple(deepcopy(matrixA))
    print('Output matrix simple method:')
    print_matrix(triangled)

    answer = gf.solve(triangled)
    error = gf.calculate_error(answer, matrixA)
    print_answer(error, answer)

    print('\n\n\n\n')
    triangled = gf.make_triangle_column(deepcopy(matrixA))
    print('Output matrix column method:')
    print_matrix(triangled)

    answer = gf.solve(triangled)
    error = gf.calculate_error(answer, matrixA)
    print_answer(error, answer)

    print('\n\n\n\n')
    triangled = gf.make_triangle_all(deepcopy(matrixA))
    print('Output matrix all method:')
    print_matrix(triangled)

    answer = gf.solve(triangled)
    error = gf.calculate_error(answer, matrixA)
    print_answer(error, answer)
