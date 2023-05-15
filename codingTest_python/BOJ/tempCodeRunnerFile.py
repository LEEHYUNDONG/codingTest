import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0


l, r = 0, 0
m = M # 임시로 삭제할 수 있는 기회
cnt = 0

while l <= r and r < N:
    # 시작점인데 왼쪽이 홀수일 경우
    if l == r and arr[l]%2:
        l += 1
        r = l
        continue
    
    if arr[r] % 2 == 0:
        cnt += 1
        r += 1
    elif arr[r]%2 != 0 and m > 0:
        r+=1
        m -= 1
    else:
        answer = max(answer, cnt)
        l = r
        cnt = 0
        m = M
answer = max(answer, cnt)


print(answer)