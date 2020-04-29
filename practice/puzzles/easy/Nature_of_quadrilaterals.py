import sys
import math


def dist_squared(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2


def dot_prod(a, b):
    return a[0]*b[0] + a[1]*b[1]


def is_parallelogram(quadr):
    side_ab = dist_squared(quadr[0],  quadr[1])
    side_ac = dist_squared(quadr[0],  quadr[2])
    side_bd = dist_squared(quadr[1],  quadr[3])
    side_cd = dist_squared(quadr[3],  quadr[2])
    return side_ab == side_cd and side_ac == side_bd


def is_rectangle(quadr):
    if not is_parallelogram(quadr):
        return False
    v1 = [quadr[1][0]-quadr[0][0], quadr[1][1]-quadr[0][1]]
    v2 = [quadr[2][0]-quadr[0][0], quadr[2][1]-quadr[0][1]]
    return dot_prod(v1, v2) == 0


def is_square(quadr):
    return is_rhombus(quadr) and is_rectangle(quadr)


def is_rhombus(quadr):
    if not is_parallelogram(quadr):
        return False
    side_ab = dist_squared(quadr[0],  quadr[1])
    side_ac = dist_squared(quadr[0],  quadr[2])
    return side_ab == side_ac


def what_is(quadr):
    if is_square(quadr):
        return "square"
    elif is_rectangle(quadr):
        return "rectangle"
    elif is_rhombus(quadr):
        return "rhombus"
    elif is_parallelogram(quadr):
        return "parallelogram"
    else:
        return "quadrilateral"


n = int(input())
for i in range(n):
    a, x_a, y_a, b, x_b, y_b, c, x_c, y_c, d, x_d, y_d = input().split()
    quadr = [[int(x_a), int(y_a)], [int(x_b), int(y_b)], [int(x_c), int(y_c)], [int(x_d), int(y_d)]]
    quadr.sort(key= lambda x: (x[0],x[1]))
    kind = what_is(quadr)
    name = a + b + c + d
    print("{} is a {}.".format(name, kind))
