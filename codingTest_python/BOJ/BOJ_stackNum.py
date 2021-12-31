import sys
input = sys.stdin.readline

n = int(input())
stack = []
cur = 1
flag = False
answer = []

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        flag = True
        break

if not flag:
    for i in answer:
        print(i)
