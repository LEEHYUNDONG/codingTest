from sys import stdin

t = int(stdin.readline())

ans = []

for _ in range(t):
    func = stdin.readline().rstrip()
    n = int(stdin.readline())
    st = stdin.readline().rstrip()
    flag = True
    cnt = 0
    if n == 0:
        l = []
    else:
        r = st[1:len(st)-1]
        r = r.split(',')
        l = [int(x) for x in r]
    for i in func:
        if i == 'D':
            if len(l) > 0:
                if cnt % 2:
                    l.pop(len(l)-1)
                else:
                    l.pop(0)
            else:
                ans.append('error')
                flag = False
                break
        if i == 'R':
            cnt += 1
    if flag:
        if cnt % 2 == 1:
            l = list(reversed(l))
        l = str(l)
        l = l.replace(" ", "")
        ans.append(l)
    l = []


for i in ans:
    print(i)
