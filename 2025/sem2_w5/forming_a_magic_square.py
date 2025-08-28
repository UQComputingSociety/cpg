#!/bin/python3

import math
import os
import random
import re
import sys

magic = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]


def rc(l):
    return [[l[2][0], l[1][0], l[0][0]],
            [l[2][1], l[1][1], l[0][1]],
            [l[2][2], l[1][2], l[0][2]]]


def flip(l):
    return [
        [l[0][2], l[0][1], l[0][0]],
        [l[1][2], l[1][1], l[1][0]],
        [l[2][2], l[2][1], l[2][0]]
    ]


all_magic = [magic,
             rc(magic),
             rc(rc(magic)),
             rc(rc(rc(magic)))]

all_magic.extend([flip(x) for x in all_magic])


def diff(l1, l2):
    return sum([abs(l1[i][j] - l2[i][j]) for i in range(3) for j in range(3)])


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    return min([diff(s, l) for l in all_magic])
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()