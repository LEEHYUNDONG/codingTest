import sys
from collections import defaultdict
input = sys.stdin.readline


g, s = map(int, input().split())
W = input().strip()
S = input().strip()

ans = 0
left = 0
right = 0
n = len(S)
k = len(W)
dictW = defaultdict(int)
dictS = defaultdict(int)

result = 0

while right < k:
    dict[W[right]] += 1
    right += 1


while left < n:
    dict[S[left]] -= 1
    if dict[S[left]] == 0:
        ans += 1
        del dict[S[left]]
    
    dict[W[right % n]] += 1
    left += 1
    right += 1


print(ans)