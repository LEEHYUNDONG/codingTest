def solution(brown, yellow):
    answer = []
    # 가로 세로 모두 yellow보다 갯수가 2개 많음
    # x-2 :yellow 가로 y-2 :yellow 세로
    # x :갈색 가로 y : 갈색 세로
    for x in range(2, brown):
        for y in range(2, x+1):
            if 2*x + 2*(y-2) == brown and (x-2) * (y-2) == yellow:
                answer.extend([x, y])
    return answer
