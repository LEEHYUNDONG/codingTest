n, m = map(int, input().split())
val = [1 for i in range(m-n+1)]  # 모든 인덱스의 값을 1로 초기화
cnt = 0
i = 2

while (i**2) <= m:  # 최대값보다 i의 제곱 값이 작아야한다.
    mul = n // i**2  # 제곱한 값에 곱할 값 처음으로 시작할 값.
    while mul * (i**2) <= m:  # 제곱한 값에 배수가 최대 값보다 작아야한다.
        if mul*(i**2)-n >= 0 and mul * (i**2) - n <= m-n:  # 배수들 지운다.
            val[mul*(i**2)-n] = 0
        mul += 1
    i += 1

print(sum(val))
