from collections import deque
import sys
input = sys.stdin.readline
bracket = input().rstrip()
q = deque(bracket)
print(q)
output = deque([])
res = 0
while q:

    tmp = q.popleft()
    if tmp == '(':
        output.appendleft(tmp)
    elif tmp == '[':
        output.appendleft(tmp)
    elif tmp == ']' and q[0] == '[':
        res *= 2
    elif tmp == ']' and q[0] == '(':


