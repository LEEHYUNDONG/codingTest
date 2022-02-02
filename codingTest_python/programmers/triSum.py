def solution(triangle):
    answer = 0

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if 1 <= i < len(triangle) and 1 <= j < len(triangle[i])-1:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            elif j == 0 and i >= 1:
                triangle[i][j] += triangle[i-1][j]
            elif i >= 1 and j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]

    return max(triangle[-1])
