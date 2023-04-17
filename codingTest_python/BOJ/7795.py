import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # A size, B size
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    A.sort()
    for i in B:
        
        # l, r = 0, N-1
        # mid = 0
        # while l <= r:
        #     mid = (l+r)//2
            
        #     if i > A[mid]:
        #         l = mid+1
        #     else:
        #         r = mid-1
        # print("B -> ", i, "l, r, mid :", l, r, mid, "N-r ->", N-r)

        # cnt += N-(r+1)
        cnt += N-bisect_right(A, i)
    
    print(cnt)

