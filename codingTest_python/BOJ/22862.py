import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = -1

for start in range(N):
    if arr[start] % 2:
        continue
    l, r = start, start
    m = M # 임시로 삭제할 수 있는 기회
    cnt = 0
    
    while r < N:
        if arr[r] % 2 == 0:
            cnt += 1
            r += 1
        elif arr[r]%2 != 0 and m > 0:
            r+=1
            m -= 1
            continue
        else:
            break
    
    answer = max(answer, cnt)

print(answer)