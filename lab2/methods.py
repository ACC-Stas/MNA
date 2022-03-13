def simple(a, b, x):
    x_temp = [0, 0, 0, 0, 0]
    for i in range(5):
        x_temp[i] = b[i]
        for j in range(5):
            if j != i:
                x_temp[i] -= a[i][j] * x[j]
        x_temp[i] /= a[i][i]
    return x_temp


def zendel(a, b, x):
    next_x = [0, 0, 0, 0, 0]
    for i in range(5):
        next_x[i] = b[i]
        for j in range(5):
            if j != i:
                if j < i:
                    next_x[i] -= a[i][j] * next_x[j]
                else:
                    next_x[i] -= a[i][j] * x[j]

        next_x[i] /= a[i][i]
    return next_x


def calculate_norm(a, b, x):
    norm = 0.0
    for j in range(0, 5):
        result = 0.0
        for i in range(0, 5):
            result += x[i] * a[j][i]
        result -= b[j]
        norm += result * result

    norm **= 0.5
    print(f"||Ax - b|| is {norm}")
    return norm
