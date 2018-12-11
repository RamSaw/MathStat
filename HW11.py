from collections import defaultdict
from math import log

import matplotlib.pyplot as plt

import numpy as np

"""
a >= 0
f(x) =
с * e^(-x), x > a
c * e^(x), x < -a
c иначе
c * (integral_{a}^{+\inf}{e^(-x)} + integral_{-\inf}^{-a}{e^(x)} + integral_{-a}^{a}{1}) = 
c * (2 * (e^(-a) - e^(-inf)) + a + a) = 2c (e^(-a) + a) = 1 <=> c = 1 / (2 * (e^(-a) + a))
---
a < 0
с * e^(-|x|)
c * 2 * e^(0) =  1 <=> c = 1 / 2
"""

a_to_set_by_user = 1
a = max(a_to_set_by_user, 0)
c = 1 / (2 * np.e ** (-a) + a)


def f(x):
    return c * np.e ** (-abs(x)) if abs(x) > a_to_set_by_user else c


def get_new_value_reverse_functions_method():
    """
    F(x) =
    a > 0
    1 - c * e^(-x), x > a
    c * (x + a + e^(-a)), x \in [-a; a]
    c * e^x, x < -a
    ---
    a <= 0
    1 - c * e^(-x), x >= 0
    c * e^x, x <= 0

    тогда G(y) =
    ln(y / c), y \in [0; c * e^(-a))
    y / c - a - e^(-a), y \in [c * e^(-a); 1 - c * e^(-a)]
    ln(c / (1 - y)), y \in (1 - c * e^(-a); 1]
    """

    def G(y):
        if 0 <= y < c * np.e ** (-a):
            return log(y / c)
        if c * np.e ** (-a) <= y <= 1 - c * np.e ** (-a):
            return y / c - a - np.e ** (-a)
        if 1 - c * np.e ** (-a) < y <= 1:
            return log(c / (1 - y))
        assert 0 <= y <= 1

    return G(np.random.uniform())


def get_new_value_reverse_for_e_x():
    def f(x):
        return np.e ** x / np.e ** (-a)

    def G(y):
        return log(y * np.e ** (-a))
    return G(np.random.uniform())


def get_new_value_reverse_for_1():
    def G(y):
        return a * (2 * y - 1)
    return G(np.random.uniform())


def get_new_value_reverse_for_e_minus_x():
    def G(y):
        return a - log(1 - y)
    return G(np.random.uniform())


def get_new_value_discrete():
    q = np.random.uniform()
    if q < c * np.e ** (-a):
        return get_new_value_reverse_for_e_x()
    if c * np.e ** (-a) <= q <= c * np.e ** (-a) + c * 2 * a:
        return get_new_value_reverse_for_1()
    if c * np.e ** (-a) + c * 2 * a < q <= c * np.e ** (-a) + c * 2 * a + np.e ** (-a) * c:
        return get_new_value_reverse_for_e_minus_x()


def draw_reverse_function_method():
    precision = 1
    conversion = "%." + str(precision) + "f"
    n = 100000
    values = defaultdict(int)
    for i in range(n):
        values[int(get_new_value_reverse_functions_method())] += 1
    data_x = []
    data_y = []
    for key in sorted(values):
        data_x.append(key)
        data_y.append(values[key])
    plt.subplot(211)
    plt.title("Reverse functions method, a = " + str(a_to_set_by_user))
    plt.plot(data_x, data_y)
    plt.ylabel("times")
    plt.xlabel("value")


def draw_discrete_method():
    precision = 1
    conversion = "%." + str(precision) + "f"
    n = 100000
    values = defaultdict(int)
    for i in range(n):
        values[int(get_new_value_discrete())] += 1
    data_x = []
    data_y = []
    for key in sorted(values):
        data_x.append(key)
        data_y.append(values[key])
    plt.subplot(212)
    plt.title("Discrete decomposition method, a = " + str(a_to_set_by_user))
    plt.plot(data_x, data_y)
    plt.ylabel("times")
    plt.xlabel("value")


def main():
    plt.figure(1)
    draw_reverse_function_method()
    draw_discrete_method()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
