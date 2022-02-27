import gauss_functions as gf
from copy import deepcopy

matrixA = [[10.300, 1.1800, 6.0200, 0.4200, -0.5300, 4.2],
           [-0.5300, 0.7300, 0.8100, 0.0700, 1.0000, 5.2],
           [3.3200, -0.5300, 4.7300, 0.8100, 3.0700, 4.2],
           [8.8900, 6.3200, -0.5300, 4.7300, -0.810, 1.2],
           [0.8100, 8.6700, 9.3200, -0.5300, 4.7300, 4.2]]

matrixB = [[5.7300, 4.0000, 2.1700, 1.5700, -0.5400, 3.2],
           [-0.6300, 4.6300, 0.6100, 3.6700, 0.6200, 1.0],
           [3.300, -0.93060, 8.7330, 3.8100, 1.0700, 4.0],
           [2.6700, 3.3200, -0.5300, 6.7300, 0.9100, 0.2],
           [6.8100, 3.6800, 5.2100, -0.4500, 4.0600, 4.2]]

matrixC = [[4.7300, 0.8100, 3.0700, 0.9200, -0.5300, 4.2],
           [-0.5300, 4.7300, 0.8100, 3.0700, 0.9200, 4.2],
           [3.3200, -0.5300, 4.7300, 0.8100, 3.0700, 4.2],
           [0.6700, 3.3200, -0.5300, 4.7300, 0.8100, 4.2],
           [0.8100, 0.6700, 3.3200, -0.5300, 4.7300, 4.2]]


def test_simple():
    triangle_a = gf.make_triangle_simple(deepcopy(matrixA))
    answer_a = gf.solve(triangle_a)
    error_a = gf.calculate_error(answer_a, matrixA)

    triangle_b = gf.make_triangle_simple(deepcopy(matrixB))
    answer_b = gf.solve(triangle_b)
    error_b = gf.calculate_error(answer_b, matrixB)

    triangle_c = gf.make_triangle_simple(deepcopy(matrixC))
    answer_c = gf.solve(triangle_c)
    error_c = gf.calculate_error(answer_c, matrixC)

    for err in error_a:
        assert err < 0.1

    for err in error_b:
        assert err < 0.1

    for err in error_c:
        assert err < 0.1


def test_column():
    triangle_a = gf.make_triangle_column(deepcopy(matrixA))
    answer_a = gf.solve(triangle_a)
    error_a = gf.calculate_error(answer_a, matrixA)

    triangle_b = gf.make_triangle_column(deepcopy(matrixB))
    answer_b = gf.solve(triangle_b)
    error_b = gf.calculate_error(answer_b, matrixB)

    triangle_c = gf.make_triangle_column(deepcopy(matrixC))
    answer_c = gf.solve(triangle_c)
    error_c = gf.calculate_error(answer_c, matrixC)

    for err in error_a:
        assert err < 0.1

    for err in error_b:
        assert err < 0.1

    for err in error_c:
        assert err < 0.1


def test_all():
    triangle_a = gf.make_triangle_all(deepcopy(matrixA))
    answer_a = gf.solve(triangle_a)
    error_a = gf.calculate_error(answer_a, matrixA)

    triangle_b = gf.make_triangle_all(deepcopy(matrixB))
    answer_b = gf.solve(triangle_b)
    error_b = gf.calculate_error(answer_b, matrixB)

    triangle_c = gf.make_triangle_all(deepcopy(matrixC))
    answer_c = gf.solve(triangle_c)
    error_c = gf.calculate_error(answer_c, matrixC)

    for err in error_a:
        assert err < 0.1

    for err in error_b:
        assert err < 0.1

    for err in error_c:
        assert err < 0.1
