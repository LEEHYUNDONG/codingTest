import sys
input = sys.stdin.readline

lst = dict()

n = int(input())
idx = 0

for i in range(n):
    book = input().strip()
    if book not in lst.keys():
        lst[book] = 1
        continue
    lst[book]+=1

res = sorted(lst.items())
res.sort(key = lambda x:x[0])
res.sort(key=lambda x:x[1], reverse=True)
print(res[0][0])