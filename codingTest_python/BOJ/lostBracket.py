import re
import sys
input = sys.stdin.readline
exp = input().strip()


num = re.findall('[\d]+', exp)
op = re.findall('[\D]', exp)

flag = False
ans = 0

for i in range(len(num)):
    if not flag:
        ans += int(num[i])
    else:
        ans -= int(num[i])
    if i < len(num) - 1:
        if op[i] == '-':
            flag = True

print(ans)