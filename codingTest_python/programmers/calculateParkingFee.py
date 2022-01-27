from collections import deque
import math


def solution(fees, records):
    answer = []
    carFee = {}
    for i in records:
        info = i.split()
        time = 60 * int(info[0][:2]) + int(info[0][3:])
        if info[1] not in carFee.keys():
            carFee[info[1]] = deque([])
            carFee[info[1]].append(time)
        else:
            carFee[info[1]].append(time)

    for i in carFee.keys():

        if len(carFee[i]) % 2:
            carFee[i].append(60*23+59)

    carFee = dict(sorted(carFee.items()))
    for i in carFee.keys():
        tt = 0
        while carFee[i]:
            iin, out = carFee[i].popleft(), carFee[i].popleft()
            tt += out - iin
        if tt <= fees[0]:
            answer.append(fees[1])
        elif tt > fees[0]:
            answer.append(fees[1]+math.ceil((tt-fees[0])/fees[2])*fees[3])

    return answer
