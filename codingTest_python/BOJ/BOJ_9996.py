import sys

n = int(input())
a, b = list(input().split('*'))
res = []
la, lb = len(a), len(b)
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    if a == tmp[0:len(a)] and b == tmp[-len(b):] and len(tmp) >= la+lb:
        res.append('DA')
    else:
        res.append('NE')

for i in res:
    print(i)
