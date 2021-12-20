n, m = map(int, input().split())

pok = dict()
num = dict()

for i in range(n):
    p = input()
    pok[p] = i+1
    num[i+1] = p

ans = []
for _ in range(m):
    t = input()
    if t.isalpha():
        ans.append(pok[t])
    else:
        ans.append(num[int(t)])

for i in ans:
    print(i)
