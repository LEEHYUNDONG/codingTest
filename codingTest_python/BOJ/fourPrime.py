import math
n = int(input())
arr = [0 for _ in range(n+1)]

for i in range(2, n+1):
    arr[i] = i

for i in range(int(math.sqrt(n+1))):
    if arr[i] == 0:
        continue
    for j in range(i+i, n+1, i):
        arr[j] = 0

answer = ''
if n < 8:
    print(-1)
# 두 수를 먼저 결정하고 나머지 숫자를 for문을 통해서 찾는다.
if n >= 8 and n % 2 == 1:
    answer = '2 3 '
    n -= 5
elif n >= 8 and n % 2 == 0:
    answer = '2 2 '
    n -= 4
for i in range(2, n+1):
    if arr[i] and arr[n-i]:
        answer += str(i)+ ' ' + str(n-i)
        print(answer)
        break