import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int , input().split()))
B = list(map(int, input().split()))
sorted_list = A + B
sorted_list.sort()
sorted_list = map(str, sorted_list)
print(' '.join(sorted_list))