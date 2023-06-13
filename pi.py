import math

digits = 1000000

import sys
sys.setrecursionlimit(digits + 10)

def calculate_pi(digits):
    pi = 0.0
    for k in range(digits):
        pi += (1 / 16**k) * (
            (4 / (8*k + 1)) -
            (2 / (8*k + 4)) -
            (1 / (8*k + 5)) -
            (1 / (8*k + 6))
        )
    return pi

pi = calculate_pi(digits)

formatted_pi = "{:.{}f}".format(pi, digits)
print(formatted_pi)
