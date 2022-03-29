import sys
input = sys.stdin.readline

n = int(input())
brr = list(map(int, input().split()))
ans = 0

while True:
    flag = False
    oper = False

    for i in range(n):
        if brr[i]:
            flag = True
        if brr[i] % 2:
            ans += 1
            oper = True
            brr[i] -= 1

    if not flag:
        break
    
    if not oper:
        for i in range(n):
            brr[i] /= 2
        ans += 1

print(ans)