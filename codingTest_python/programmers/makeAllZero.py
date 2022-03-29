import copy
import sys
sys.setrecursionlimit(10**8)
answer = 0
tot = 0

def solution(a, edges):
    
    if sum(a) != 0:
        return -1
    global answer
    graph = [[]*len(a) for _ in range(len(a))]
    
    for b, c in edges:
        graph[b].append(c)
        graph[c].append(b)
    
    visited = [False]*len(a)
    
    def dfs(start, a, size):
        global answer
        visited[start] = True
        
        for i in graph[start]:
            if not visited[i]:

                a[start] += dfs(i, a, size)
        
        answer += abs(a[start])
        return a[start]
                
                

    dfs(0, a, len(a))
    
        
    return answer