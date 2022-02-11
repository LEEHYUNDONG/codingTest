import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
checked = [0]*m
positions = [0]*n

time = 0
count = 0
crane.sort(reverse=True)
boxes.sort(reverse=True)

if max(boxes) > max(crane):
    print(-1)
else:
    while count < len(boxes):
        for i in range(n):
            while positions[i] < len(boxes):
                if not checked[positions[i]] and crane[i] >= boxes[positions[i]]:
                    checked[positions[i]] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
            print(positions)
        time += 1
    print(time)