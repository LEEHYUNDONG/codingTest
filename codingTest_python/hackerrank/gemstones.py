#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#


def gemstones(arr):

    s1 = set(arr[0])
    for i in range(len(arr)-1):
        s2 = set(arr[i+1])
        s1 = s2.intersection(s1)
        print(s1)

    return len(s1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
