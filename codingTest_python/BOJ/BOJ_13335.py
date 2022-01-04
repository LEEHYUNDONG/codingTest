import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
trucks = deque(truck)
dep = deque()
bridge = deque()
time = 0

while bridge or trucks:
    time += 1
    if bridge:  # 다리에 트럭ㅣ 있을때
        if dep[0] + w == time:  # 들어간 시간에서 w를 더하면 나올 시간
            bridge.popleft()
            dep.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.popleft())
            dep.append(time)

print(time)
