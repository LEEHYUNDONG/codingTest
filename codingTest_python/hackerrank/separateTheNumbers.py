#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):
    if len(s) == 1:
        print("NO")
        return

    for i in range(1, (len(s)//2)+1):
        idx = 0
        l = i
        lst = []
        tmp = ''
        flag = True
        while idx < len(s):
            t = idx
            for j in range(t, l+t):
                tmp += s[idx]
                idx += 1
                if idx == len(s):
                    break
            lst.append(tmp)
            if tmp != '' and tmp[-1] == '9' and len(set(tmp)) == 1:
                l += 1
            tmp = ''
        # print(lst)
        for j in range(len(lst)-1):
            if not lst[j].startswith('0') and not lst[j+1].startswith('0'):
                if int(lst[j])+1 == int(lst[j+1]):
                    flag = True
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            print("YES", lst[0])
            return
    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
