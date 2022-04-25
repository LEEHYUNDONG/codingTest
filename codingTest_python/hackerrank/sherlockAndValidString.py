#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def isValid(s):
    cdic = Counter(s)
    c = cdic.most_common()
    dic = dict()
    flag = False
    for i in c:
        if i[-1] not in dic.keys():
            dic[i[-1]] = [i[0]]
            continue
        dic[i[-1]].append(i[0])

    if len(dic.keys()) > 2:
        return "NO"
    elif len(dic.keys()) == 1:
        return "YES"
    elif len(dic.keys()) == 2:
        k = list(dic.keys())
        if ((len(dic[k[0]]) == 1) or (len(dic[k[-1]]) == 1)):
            if k[0] == 1 or k[-1] == 1 or abs(k[-1]-k[0]) == 1:
                if k[0] == 1 and len(dic[k[0]]) > 1:
                    return "NO"
                if k[-1] == 1 and len(dic[k[-1]]) > 1:
                    return "NO"

                return "YES"

        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
