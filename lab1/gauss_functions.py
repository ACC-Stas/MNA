def exchange(matrix, k):
    max_ = abs(matrix[k][k])
    max_i = k
    for i in range(k + 1, 5):
        if abs(matrix[i][k]) > max_:
            max_ = abs(matrix[i][k])
            max_i = i
    if max_i != k:
        tmp = matrix[k]
        matrix[k] = matrix[max_i]
        matrix[max_i] = tmp


def make_triangle_column(matrix):
    for i in range(5):
        exchange(matrix, i)
        if matrix[i][i] != 0:
            a = matrix[i][i]
            for j in range(i + 1, 5):
                q = matrix[j][i] / a
                for k in range(i, 6):
                    matrix[j][k] -= matrix[i][k] * q
                    matrix[j][k] = round(matrix[j][k], 8)
    return matrix


def make_triangle_all(matrix):
    n = len(matrix)
    for k in range(n - 1):
        exchange(matrix, k)
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]
            matrix[i][-1] = round(matrix[i][-1], 4)
            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]
                matrix[i][j] = round(matrix[i][j], 4)
    print()
    return matrix


def make_triangle_simple(matrix: list[list[float]]) -> list[list[float]]:
    for i in range(5):
        if matrix[i][i] != 0:
            a = matrix[i][i]
            for j in range(i + 1, 5):
                q = matrix[j][i] / a
                for k in range(i, 6):
                    matrix[j][k] -= matrix[i][k] * q
                    matrix[j][k] = round(matrix[j][k], 4)
        elif i != 4:
            tmp = matrix[i]
            matrix[i] = matrix[i + 1]
            matrix[i + 1] = tmp
            i -= 1
    return matrix


def solve(matrix: list[list[float]]) -> list[float]:
    answer = list(range(5))
    for i in range(4, -1, -1):
        for j in range(4, i, -1):
            matrix[i][5] -= answer[j] * matrix[i][j]
            j -= 1

        answer[i] = round(matrix[i][5] / matrix[i][i], 8)

    return answer


def calculate_error(answer: list[float], default_matrix: list[list[float]]) -> list[float]:
    error: list[float] = []
    for i, row in enumerate(default_matrix):
        error.append(0)
        for j in range(0, len(row) - 1):
            error[i] += row[j] * answer[j]

        error[i] = (abs(error[i] - row[len(row) - 1]))

    return error
