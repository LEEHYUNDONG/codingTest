import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    lst = dict()
    for i in set(s):
        if i.isalpha():
            if i.islower():
                lst[i] = chr(ord('a')+(((ord(i)-ord('a')+k)) % 26))
            elif i.isupper():
                lst[i] = chr(ord('A')+(((ord(i)-ord('A')+k)) % 26))
    tmp = ''
    for key in s:
        if key in lst.keys():
            tmp += lst[key]
        else:
            tmp += key

    return tmp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
