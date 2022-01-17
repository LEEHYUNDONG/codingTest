def solution(rows, columns, queries):
    answer = []
    arr = [[(i-1)*columns+j for j in range(1, columns+1)]
           for i in range(1, rows+1)]

    for x, y, rx, ry in queries:
        top, left, bottom, right = x-1, y-1, rx-1, ry-1
        tmp = arr[top][left]
        minV = tmp
        for i in range(left+1, right+1):
            minV = min(tmp, minV)
            prev = arr[top][i]
            arr[top][i] = tmp
            tmp = prev

        for i in range(top+1, bottom+1):
            minV = min(tmp, minV)
            prev = arr[i][right]
            arr[i][right] = tmp
            tmp = prev

        for i in range(right-1, left-1, -1):
            minV = min(tmp, minV)
            prev = arr[bottom][i]
            arr[bottom][i] = tmp
            tmp = prev

        for i in range(bottom-1, top-1, -1):
            x = i
            minV = min(tmp, minV)
            prev = arr[i][left]
            arr[i][left] = tmp
            tmp = prev

        minV = min(tmp, minV)
        answer.append(minV)

    return answer


solution(6, 6, [
    [2, 2, 5, 4],
    [3, 3, 6, 6],
    [5, 1, 6, 3]
])
