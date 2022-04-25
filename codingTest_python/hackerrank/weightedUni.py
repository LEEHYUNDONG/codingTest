#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#


def weightedUniformStrings(s, queries):
    # Write your code here
    ans = []
    alphaDic = dict()
    l = 1
    board = set()
    for i in range(26):
        alphaDic[chr(i+ord('a'))] = i+1

    for i in range(len(s)):
        score = alphaDic[s[i]]
        if i+1 != len(s) and s[i+1] == s[i]:
            l += 1
        else:
            l = 1
        board.add(score*l)
    for i in queries:
        if i in board:
            ans.append("Yes")
        else:
            ans.append("No")
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
