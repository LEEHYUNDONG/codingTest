import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

ans = 0
crane.sort(reverse=True)
boxes.sort(reverse=True)

while boxes:
    flag = False
    for i in range(len(crane)):
        if boxes and crane[i] >= boxes[0]:
            flag = True
            boxes.pop(0)

    if not flag:
        ans = -1
        break
    ans += 1

print(ans) 