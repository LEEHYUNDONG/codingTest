'''
0-빈칸
6-벽

cctv 1 ~ 5
1번 4가지 경우
2번 2가지
3번 4가지
4번 4가지
5번 1가지
총 경우의수
4*2*4*4 = 128가지 경우의 수 * cctv 대수

취대 128*8
1000미만
1. cctv 위치 파악, 감시 구역 퍼뜨리는것 모든 경우 계산
2. 여러 경우에서 사각지대 탐색 dfs
'''

import sys
input = sys.stdin.readline
from collection import deque
from copy import deepcopy

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
directions = [
    [], 
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
    [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]],
    [[0, 1, 2, 3]]
]

visited = [[False for _ in range(M)] for _ in range(N)]
cnt = 0
ccnt = 0
answer = 0
cctv = []

def check(rx, ry):
    return 0 <= rx < N and 0 <= ry < M and not visited[rx][ry] and graph[rx][ry] == 0

# 감시되지 않는 영역 count
def countArea(x, y, depth):
    global cnt
    
    cnt += 1

    for i in range(4):
        rx, ry = x + dx[i], y + dy[i]
        if check(rx, ry):
            countArea(rx, ry, depth+1)

# 감시 구역 확산
def watch(x, y, direction, tmp):
    for i in direction:

# cctv 위치 확보
for i in range(N):
    for j in range(M):
        if 1<= graph[i][j] <= 5:
            cctv.append((i, j, graph[i][j]))

def tot_Area(graph):
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 0:
                cnt = 0
                countArea(i, j, 1)
                ccnt += cnt
            
print(ccnt)
