import re

exp = input().strip()


num = re.findall('[\d]+', exp)
op = re.findall('[\D]', exp)

if len(op) == 1:
    if op == '+':
        print(int(num[0])+int(num[-1]))
    else:
        print(int(num[0])-int(num[-1]))

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