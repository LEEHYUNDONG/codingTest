# https://www.acmicpc.net/problem/1614
N = int(input()) # N번째 손가락
chance = int(input()) # 사용할 수 있는 기회
ans = 0

if chance == 0:
    print(N-1)

elif N == 5:
    print(8*chance+4)
elif N == 4:
    if chance % 2 == 1:
        print(8*(chance//2+1)-3)
    else:
        print(8*(chance//2)+3)

elif N == 3:
    print(4*chance + 2)
elif N == 2:
    if chance % 2 == 1:
        print(8*(chance//2+1)-1)
    else:
        print(8*(chance//2)+1)
elif N == 1:
    print(8*chance)
