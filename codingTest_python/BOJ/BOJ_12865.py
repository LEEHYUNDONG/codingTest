# # 평범한 배낭
# from collections import deque

# n = int(input())
# directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
# graph = [list(input()) for _ in range(n)]
# visited = [[False ] * n] * n
# def run():
#     cnt = 1
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j]:
#                 print("i, j :", i, j)
#                 bfs(i, j)
#                 cnt += 1
#     return cnt

# def bfs(x, y):
#     queue = deque([])
#     queue.append((x, y, graph[x][y]))
#     #visited[x][y] = True
#     while queue:
#         x, y, c = queue.popleft()
#         visited[x][y] = True
#         for dx, dy in directions:
#             #print(x, y, c)
#             rx, ry = x+dx, y+dy
#             if (0 <= rx < n) and (0 <= ry < n):
#                 print("x, y, c :",x, y, c)
#                 print("rx, ry :",rx, ry, graph[rx][ry])
#                 if graph[rx][ry] != graph[x][y]:
#                      continue
#                 if not visited[rx][ry]:
#                     if graph[rx][ry] == c:   
#                         queue.append((rx, ry, graph[rx][ry]))
                        
#                         visited[rx][ry] = True
                
#     print(visited)                
# ans1= run()
# print(ans1)
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(matrix)
def dfs(x,y):
    #현재 색상 좌표를 방문해준다.
    visited[x][y] = True
    current_color = matrix[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visited[nx][ny]==False:
                if matrix[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if visited[i][j]==False:
            dfs(i,j)
            three_cnt += 1

#R을 G로 바꾸어준다. --> 적록색약은 같은 색으로 보기 때문에
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='R':
            matrix[i][j]='G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)