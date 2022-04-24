import numpy
import sympy

m = 0.1
a = 0.8
eps = 10.0 ** -5
iterations = 0


def main():
    print("\033[96mСистема нелинейных уравнений:")
    (x, y) = sympy.symbols("x y")
    eq1 = sympy.tan(x * y + m) - x
    eq2 = a * (x ** 2) + 2 * (y ** 2) - 1
    print(eq1, "= 0")
    print(eq2, "= 0", end='\n\n')
    x0 = 0.6
    y0 = 0.5
    print("\033[94mНачальное приближение: ", (x0, y0), end='\n\n\033[0m')
    plots = sympy.plot_implicit(sympy.Eq(eq1, 0), (x, -2, 2), (y, -2, 2), line_color="blue", show=False)
    plots.extend(sympy.plot_implicit(sympy.Eq(eq2, 0), (x, -2, 2), (y, -2, 2), line_color="red", show=False))
    test(simple_iterations, x0, y0)
    test(newton, x0, y0)
    plots.show()


# Подстановка в исходные уравнения для вычисления значения f(x,y)
def val1(x, y):
    return numpy.tan(x * y + m) - x


def val2(x, y):
    return a * (x ** 2) + 2 * (y ** 2) - 1


# Выраженные из исходных уравнений x = функция(x,y), y = функция(x, y)
def eq_x(x, y):
    return numpy.tan(x * y + m)


def eq_y(x, y):
    return numpy.sqrt((1 - a * (x ** 2)) / 2)


# Вычисление матрицы Якоби
def W(x, y):
    return numpy.array(
        [[(1 + numpy.tan(x * y + m) ** 2) * y - 1, (1 + numpy.tan(x * y + m) ** 2) * x], [2 * a * x, 4 * y]])


def simple_iterations(x0, y0):
    global iterations
    iterations = 0
    (x, y) = (x0, y0)
    while True:
        iterations += 1
        old_x = x
        old_y = y
        x = eq_x(x, y)
        y = eq_y(x, y)
        if not (numpy.isfinite(x) and numpy.isfinite(y)):
            raise RuntimeError("Последовательность {x} расходится")
        if max(abs(x - old_x), abs(y - old_y)) < eps:
            return x, y


def newton(x0, y0):
    global iterations
    iterations = 0
    (x, y) = (x0, y0)
    while True:
        iterations += 1
        f = numpy.array([[val1(x, y)], [val2(x, y)]])
        deltas = numpy.linalg.solve(W(x, y), -f)
        x += deltas[0][0]
        y += deltas[1][0]
        if not (numpy.isfinite(x) and numpy.isfinite(y)):
            raise RuntimeError("Последовательность {x} расходится")
        if max(abs(deltas)) < eps:
            return x, y


def test(method, x0, y0):
    global iterations
    try:
        (x, y) = method(x0, y0)
        print("\033[92m(x, y) = ({:.4f}, {:.4f})".format(x, y))
        print("с помощью метода {} ({} итераций)".format(method.__name__, iterations))
    except Exception as ex:
        print("Ошибка: {} - в методе {} method ({} итераций)".format(ex, method.__name__, iterations))
        print()


if __name__ == '__main__':
    main()
