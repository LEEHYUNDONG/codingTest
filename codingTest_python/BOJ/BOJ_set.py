import sys
input = sys.stdin.readline

n = int(input())
b = 0
ans = []


for i in range(n):
    tmp = input().rsplit()
    op = tmp[0]
    if op == "add":
        num = int(tmp[1])
        b = (1 << num) | b
    elif op == "check":
        num = int(tmp[1])
        if (1 << num) & b:
            print(1)
        else:
            print(0)
    elif op == 'remove':
        num = int(tmp[1])
        b = b & ~(1 << int(num))
    elif op == 'toggle':
        num = int(tmp[1])

        b = (1 << num) ^ b
    elif op == 'all':
        b = (1 << 21) - 1
    elif op == 'empty':
        b = 0
