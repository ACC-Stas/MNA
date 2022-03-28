import sympy as sp
import methods as met
from sympy.abc import x
from sympy.plotting import plot


def print_plot(left_border=None, right_border=None):
    plot1 = plot(x ** 3 + a * x ** 2 + b * x + c, left_border, right_border, show=False)
    plot1[0].line_color = 'green'
    plot1.show()
    return


if __name__ == "__main__":
    a = sp.Float(15)
    b = sp.Float(1)
    c = sp.Float(40)
    base_poly = sp.poly(x ** 3 + a * x ** 2 + b * x + c)

    print("Количество корней на заданном промежутке:")
    amount = met.find_root_amount(base_poly, -10, 10)
    print(amount)
    print_plot(left_border=-10, right_border=10)
    print()

    if amount != 0:
        print("Х, кол-во итераций")
        print("Метод половинного деления: ", met.bisection_method(base_poly, -5, -2.5, 1e-5))
        print()

        print("Метод хорд: ", met.chord_method(base_poly, -5, -2.5, 1e-5))
        print()

        print("Метод Ньютона: ", met.newton_method(base_poly, -5, 1e-5))
