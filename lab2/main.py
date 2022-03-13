import methods
import numpy as np
import copy


def solve(method, a, b, x, need_accuracy=0.0001):
    iteration_number = 0
    if x is None:
        x = [0, 0, 0, 0, 0]

    while iteration_number >= 0:
        next_x = method(a, b, x)
        norm = methods.calculate_norm(a, b, x)
        iteration_number += 1
        x = copy.deepcopy(next_x)
        if norm < need_accuracy:
            for i in range(5):
                print(f"x{i} = {x[i]:.4f}")
            break
        else:
            print(f"Number of iterations: {iteration_number}")
    print()


def main():
    a = [[1.39, 0.21, 0.05, 0.12, -0.13],
         [-0.07, -1.27, -0.01, 0.17, 0.12],
         [0.12, -0.07, -1.27, 0.11, 0.05],
         [0.17, 0.12, -0.07, -1.27, 0.11],
         [0.11, 0.67, 0.12, -0.07, -1.27]]

    ba = [1.2, 2.2, 4.0, 0.0, -1.2]

    d = [[0.7, 0, 0.23, 0.11, -0.12],
         [0.5, 1.11, 0, -0.56, 0],
         [1, 0.01, 2, 0, 1],
         [0.03, 0, 0.12, 1.33, -0.03],
         [-0.15, 0.34, 0, 0, 1.34]]

    bd = [1.2, 1.1, 1.0, 0.0, -1.2]

    e = [[0.2, 0, 0.07, -0.11, 0.12],
         [0.66, 1.89, 0, -0.56, 0],
         [1, 0.55, -2, 0, 1],
         [0.3, -0.14, 0.12, 1.74, 0.17],
         [-0.15, 0.34, 0, 0, 0.67]]

    be = [1.2, 1.1, 1.0, 0.0, -1.2]
    print(np.array(a))

    print("Simple method")
    solve(methods.simple, a, ba, None)
    print("Zendel method")
    solve(methods.zendel, a, ba, None)

    print("Simple method")
    solve(methods.simple, d, bd, None)
    print("Zendel method")
    solve(methods.zendel, d, bd, None)

    print("Simple method")
    solve(methods.simple, e, be, None)

    print("Zendel method")
    solve(methods.zendel, e, be, None)


if __name__ == '__main__':
    main()
