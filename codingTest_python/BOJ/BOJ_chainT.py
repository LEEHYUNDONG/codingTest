import sys
from collections import deque
input = sys.stdin.readline

# 톱니 바퀴 갯수
t = int(input())
tob = [list(input().strip()) for _ in range(t)]
tq = deque([])

for i in range(t):
    tq.append(deque(tob[i]))

# 회전횟수 k
k = int(input())
# 첫 번째 정수 톱니바퀴 번호, 두 번째 정수 회전 방향
operation = [list(map(int, input().split())) for _ in range(k)]

# 시계방향 1, 반시계 -1 각 번호로 부터 번호가 짝 홀이냐에 따라서 회전이 달라짐
# 짝수가 시계방향 -> 홀수 반시계 방향,짝수 반시계 -> 홀수 시계방향
# 첫 번째 인덱스 12시 방향부터 시계방향 순으로 하나씩 뒤로 당기거나 앞으로 당기는 거 구현하셈
# 0, 2,  6
# 12시, 3시, 9시
left, right = 2, 6
for op in operation:
    num, wise = op
    num -= 1
    cur_direction = wise
    cur_left, cur_right = tq[num][left], tq[num][right]
    tq[num].rotate(wise)

    for i in reversed(range(num)):
        if cur_right == tq[i][left]:
            break
        elif cur_right != tq[i][left]:
            cur_right = tq[i][right]
            tq[i].rotate(cur_direction*-1)
            cur_direction *= -1

    cur_direction = wise
    for i in range(num+1, t):
        if tq[i][right] == cur_left:
            break
        elif tq[i][right] != cur_left:
            cur_left = tq[i][left]
            tq[i].rotate(cur_direction*-1)
            cur_direction *= -1


cnt = 0
for i in range(t):
    if tq[i][0] == '1':
        cnt += 1
print(cnt)