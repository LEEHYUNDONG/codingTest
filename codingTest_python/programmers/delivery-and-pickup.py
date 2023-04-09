def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0

    for i in range(n-1, -1, -1):

        cnt = 0

        d -= deliveries[i]
        p -= pickups[i]

        while d < 0 or p < 0:
            d += cap
            p += cap
            cnt += 1

        answer += (i + 1) * 2 * cnt

    return answer


'''
def solution(cap, n, deliveries, pickups):
    answer = 0
    houses = len(deliveries)
    # 배달지와 픽업과 거리별로 데이터를 묶음
    dist = [i for i in range(1, n+1)]
    last = n-1
    
    while deliveries or pickups:
        # 적재 가능한 박스 수
        box = cap
        # 거리 계산
        answer += len(deliveries)
        
        # 첫번째 반복문은 배달
        for i in range(len(deliveries)-1, -1, -1):
            if deliveries[i] < box and deliveries[i] < cap:
                box -= deliveries[i]
                deliveries.pop()
            else:
                deliveries[i] -= box
                if deliveries[i] == 0:
                    deliveries.pop()
                break

        # 적재 가능한 박스 수
        box = 0
        answer += len(pickups)
        
        # 두번째 반복문은 배달지에서 복귀, 수거
        for i in range(len(pickups)-1, -1, -1):
            # 박스 수거시 현재 차 안에 있는 수거할 박스가 cap보다 작을때
            if box < pickups[i] and pickups[i] < cap:
                box += pickups[i]
                pickups.pop()
            else:
                pickups[i] -= (cap-box)
                if pickups[i] == 0:
                    pickups.pop()
                break
        
    
    
    return answer

'''