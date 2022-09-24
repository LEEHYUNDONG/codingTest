from collections import deque
import heapq
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    dq = deque([])

    # 배달 수거를 반복하며 dq가 비면 완료
    for i in range(n):
        dq.append([deliveries[i], pickups[i]])

    print(dq)
    while dq:
        answer += len(dq)
        tCap = cap

        #배달 뒤에서 부터
        for i in range(len(dq)-1, -1, -1):
            
            tCap -= dq[i][0]
            dq[i][0] = 0
            if tCap == 0:
                break
                    
        answer += len(dq)
        # 수거 앞에서 부터

    
    
    return answer