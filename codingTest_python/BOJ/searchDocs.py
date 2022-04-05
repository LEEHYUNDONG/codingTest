import sys
input = sys.stdin.readline
s = input().strip()
target = input().strip()

cnt = 0
i = 0

while True:
    if (s.find(target) == -1): break
    s = s.replace(target, '*', 1)

print(s.count('*'))