import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        # x, y는 돌려지는 배열중 가장 첫번째 배열 인덱스
        x, y = i, i
        tmp = arr[x][y]
        
        # 안쪽까지 계속 계산을 해줘야하기 때문에 n-i, m-i까지가 범위가 된다.
        for j in range(i+1, n-i): #좌
            x = j
            prev = arr[x][y]
            arr[x][y] = tmp
            tmp = prev
        
        for j in range(i+1, m-i): #하
            y = j
            prev = arr[x][y]
            arr[x][y] = tmp
            tmp = prev
        
        for j in range(i+1, n-i): #우
            x = n - j - 1
            prev = arr[x][y]
            arr[x][y] = tmp
            tmp = prev

        for j in range(i+1, m-i) : #상
            y = m-j-1
            prev = arr[x][y]
            arr[x][y] = tmp
            tmp = prev
        
        
for i in range(n):
    print(*arr[i])