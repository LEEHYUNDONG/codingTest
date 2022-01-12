import sys
input = sys.stdin.readline

n = int(input())
bud = list(map(int, input().split()))
target = int(input())
start, end = 0, max(bud)
bud.sort()

while start <= end:
    mid = (start + end)//2
    tot = 0
    for i in bud:
        tot += min(mid, i)

    # if tot > target:
    #     end = mid - 1
    # else:
    #     start = mid + 1
    #     ans = mid
    if tot <= target:
        start = mid + 1
        ans = mid
    elif tot > target:
        end = mid - 1

# 왜 if문의 순서를 다르게하면 틀렸습니다가 나오는지 알아보기
print(ans)
