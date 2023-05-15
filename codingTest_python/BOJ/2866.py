import sys

input = sys.stdin.readline
R, C = map(int, input().split())
table = [list(input().strip()) for _ in range(R)]

print(table)