import heapq

def solution(n, works):
    answer = 0
    q = []
    
    for i in works:    
        heapq.heappush(q, -i)
    
    for i in range(n):
        item = heapq.heappop(q)
        if item < 0:
            item += 1
            heapq.heappush(q, item)
        else:
            break
        
        
    for work in q:
        answer += work**2
    
    return answer