import sys
input = sys.stdin.readline
t = int(input())
num = []
ans = []
for _ in range(t):
    num.append(int(input()))

arr = [i for i in range(max(num)+1)]
arr[0], arr[1] = 0, 0

for i in range(max(num)+1):
    if arr[i] == 0:
        continue
    for j in range(i+i, max(num)+1, i):
        arr[j] = 0

for i in num:
    tmp = []
    a = i//2
    b = i//2
    for j in range(i):
        if arr[a] and arr[b] and a + b == i:
            ans.append([a, b])
            break
        a -= 1
        b += 1
                
for i in ans:
    print(*i)