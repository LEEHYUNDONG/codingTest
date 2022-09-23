import sys

input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]


data.sort(key = lambda x : (x[1], x[0]))

for d in data:
    print(*d)