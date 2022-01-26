def zipQuad(arr, visited, x, y, size):
    global ans
    color = arr[x][y]
    flag = True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != arr[i][j] and not visited[i][j]:
                zipQuad(arr, visited, x, y, size//2)
                zipQuad(arr, visited, x+size//2, y, size//2)
                zipQuad(arr, visited, x, y + size//2, size//2)
                zipQuad(arr, visited,  x + size//2, y + size//2, size//2)
                flag = False
    if flag:
        for i in range(x, x+size):
            for j in range(y, y+size):
                visited[i][j] = True
        ans[color] += 1

    return


ans = [0, 0]


def solution(arr):
    visited = [[False]*len(arr) for _ in range(len(arr))]
    zipQuad(arr, visited, 0, 0, len(arr))
    return ans
