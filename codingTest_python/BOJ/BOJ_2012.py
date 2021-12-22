# 등수 매기기
n = int(input())
rank = []

for i in range(n):
    rank.append(int(input()))

rank.sort()
res = 0

for i in range(n):
    res += abs((i+1)-rank[i])
print(res)
