import math
from math import sqrt


def is_sqrt(seq):
    new_list = []
    for i in seq:
        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i:
            new_list.append(i)

    print(new_list)


seq = [49, 8, 2, 1, 102]
is_sqrt(seq)
seq = [500, 30]
is_sqrt(seq)
