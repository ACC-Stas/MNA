import math


def make_step(a, e):
    b = a
    h = e
    mI = 0
    mJ = 1
    maxEl = a[0][1]

    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a[i])):
            if abs(a[i][j]) > abs(maxEl):
                maxEl = a[i][j]
                mI = i
                mJ = j

    if a[mI][mI] != a[mJ][mJ]:
        fi = 0.5 * math.atan(2 * maxEl / (a[mI][mI] - a[mJ][mJ]))
    else:
        fi = math.pi / 4
    c = math.cos(fi)
    s = math.sin(fi)
    b[mI][mI] = c ** 2 * a[mI][mI] + s ** 2 * a[mJ][mJ] + 2 * c * s * a[mI][mJ]
    b[mJ][mJ] = s ** 2 * a[mI][mI] + c ** 2 * a[mJ][mJ] - 2 * c * s * a[mI][mJ]
    for k in range(0, len(a)):
        h[mI][k] = c * e[k][mI] - s * e[k][mJ]
        h[mJ][k] = s * e[k][mI] + c * e[k][mJ]
        if k == mI or k == mJ:
            continue
        b[mI][k] = c * a[k][mI] + s * a[k][mJ]
        b[k][mI] = b[mI][k]
        b[mJ][k] = -s * a[k][mI] + c * a[k][mJ]
        b[k][mJ] = b[mJ][k]
        b[mI][mJ] = b[mJ][mI] = 0
    return b, h


def is_over(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a[i])):
            if a[i][j] != 0:
                return True
    return False


def print_matrix(a, b):
    for i in range(0, len(a)):
        a[i][i] = round(a[i][i], 4)
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            b[i][j] = round(b[i][j], 4)

    print('Собственные значения матрицы:')
    for i in range(0, len(a)):
        print(a[i][i])

    print('\nСобственные вектора:')
    for j in range(0, len(b)):
        print('[  ', end='')
        for i in range(0, len(b[j])):
            print(b[i][j], end='  ')
        print(']')


if __name__ == "__main__":
    matrix = [[3.53, 0.81, 1.87, 0.92, -0.53],
              [-0.53, 3.53, 0.81, 1.87, 0.92],
              [2.12, -0.53, 3.53, 0.81, 1.87],
              [0.67, 2.12, -0.53, 3.53, 0.81],
              [0.81, 0.67, 2.12, -0.53, 3.53]]

    e = [[1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1]]

    while is_over(matrix):
        matrix, e = make_step(matrix, e)
    print_matrix(matrix, e)
