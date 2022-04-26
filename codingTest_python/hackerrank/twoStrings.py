#!/bin/python3

import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    stmp1 = set(s1)
    stmp2 = set(s2)
    return "YES" if len(stmp1.intersection(stmp2)) >= 1 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
