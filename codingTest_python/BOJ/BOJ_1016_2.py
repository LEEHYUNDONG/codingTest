# 시간 초과
n, m = map(int, input().split())
val = [1 for i in range(m+1)]  # 모든 인덱스의 값을 1로 초기화
cnt = 0

for i in range(n, m+1):
    if val[i] == 0:
        continue
    for j in range(i+i, m, i):
        val[j] = 0

print(m-n+1-sum(val))
