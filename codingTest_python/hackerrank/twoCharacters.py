#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
import copy

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def checkAlternating(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

def alternate(s):
    lst = set(s)
    ans = 0
    if len(lst) == 1 or len(lst) == 2:
        if len(lst) == 2 and checkAlternating(s):
            ans = max(ans, len(s))
        return ans
    for combi in combinations(lst, len(lst)-2):
        tmp = copy.deepcopy(s)
        for i in combi:
            tmp = tmp.replace(i, '')
        if checkAlternating(tmp):
            ans = max(ans, len(tmp))
            # print(tmp, combi)
    return ans
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
