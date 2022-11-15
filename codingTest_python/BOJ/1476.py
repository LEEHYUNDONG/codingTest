import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

E, S, M = map(int, input().split())


def dfs(e, s, m, depth):
    global ans
    if e == E and s == S and m == M:
        print(depth)
        return
    
    dfs(e%15+1, s%28+1, m%19+1, depth+1)

dfs(1, 1, 1, 1)
