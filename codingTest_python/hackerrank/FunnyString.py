#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def funnyString(s):
    tmp = []
    for i in range(len(s)-1):
        tmp.append(abs(ord(s[i])-ord(s[i+1])))
    l, r = 0, len(tmp)-1
    while l < r:
        if tmp[l] != tmp[r]:
            return "Not Funny"
        l += 1
        r -= 1
    return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
