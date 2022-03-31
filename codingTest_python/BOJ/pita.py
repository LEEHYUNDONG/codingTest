import math

b = int(input())

tmp = b**2

for i in range(1, b+1):
    res = (i**2+tmp)**0.5
    ttmp = int(res)
    if ttmp == res:
        print(ttmp)
        exit()

print(-1)
