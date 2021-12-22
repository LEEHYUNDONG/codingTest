#길찾기 게임
def solution(nodeinfo):
    answer = [[]]
    n = len(nodeinfo)
    graph = [[] for _ in range(n)]
    tmp = []

    for i in range(n):
        tmp.append([nodeinfo[i][0], nodeinfo[i][1], i+1])
    
    tmp = sorted(tmp, key=lambda x:x[1], reverse=True)
    
    for i in range(n):
        for j in range(n):
            #if graph[i][1] 
    
    print(tmp)
    

    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(nodeinfo)
    