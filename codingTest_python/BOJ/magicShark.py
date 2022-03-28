import sys
input = sys.stdin.readline

n, q = map(int, input().split())
size = 2**n
graph = [list(map(int, input().split())) for _ in range(size)]

def rotate