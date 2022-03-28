import sympy as sp
from sympy.abc import x


def find_root_amount(poly=None, left_border=None, right_border=None):
    def calculate_shturm_value(_poly_range_, value):
        counter = 0
        size = len(_poly_range_)
        current_sgn = _poly_range_[0](value) > 0
        for i in range(size - 1):
            new_sgn = _poly_range_[i + 1](value) > 0
            if new_sgn != current_sgn:
                counter += 1
            current_sgn = new_sgn
        return counter

    shturm_sequence = [poly, sp.diff(poly)]
    sequence_range = sp.degree(poly, gen=x)
    for i in range(sequence_range - 1):
        shturm_sequence.append(-sp.div(shturm_sequence[i], shturm_sequence[i + 1])[1])
    return calculate_shturm_value(shturm_sequence, left_border) - calculate_shturm_value(shturm_sequence, right_border)


def bisection_method(poly, left_border, right_border, accuracy):
    global average
    counter = 0
    while abs((left_border - right_border)) > accuracy:
        average = (left_border + right_border) / 2
        if poly(left_border) * poly(average) <= 0:
            right_border = average
        else:
            left_border = average
        counter += 1
    return average, counter


def chord_method(poly, left_border, right_border, accuracy):
    temp = 0
    average = 10 * accuracy
    counter = 0
    while abs(temp - average) > accuracy:
        temp = average
        average = left_border - (poly(left_border) / (poly(right_border) - poly(left_border))) * (
                right_border - left_border)
        if poly(left_border) * poly(average) <= 0:
            right_border = average
        else:
            left_border = average
        counter += 1
    return average, counter


def newton_method(poly, entrypoint, accuracy):
    derivative_func = sp.diff(poly)
    previous = entrypoint + accuracy * 10
    counter = 0
    while abs(entrypoint - previous) > accuracy:
        previous = entrypoint
        entrypoint = entrypoint - poly(entrypoint) / derivative_func(entrypoint)
        counter += 1
    return entrypoint, counter
