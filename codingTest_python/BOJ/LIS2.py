import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rsplit()))
lis = []
ans = 0

for num in arr:
    if not lis: #비어있으면 리스트에 추가
        lis.append(num)
        ans += 1
        continue
    
    # 마지막 숫자보다 큰 수라면 추가 
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    # 숫자가 같거나 작은 수가 나온다면 특정 위치에 재삽입
    else:
        index = bisect_left(lis, num)
        lis[index] = num
    
print(ans)