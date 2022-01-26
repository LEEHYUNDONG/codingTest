def zipQuad(arr, visited, x, y, size):
    global ans
    color = arr[x][y]
    if size == 1:
        ans[arr[x][y]] += 1
        return
    else:
        for i in range(x, x+size):
            for j in range(y, y+size):
                if color != arr[i][j]:
                    zipQuad(arr, visited, x, y, size//2)
                    zipQuad(arr, visited, x+size//2, y, size//2)
                    zipQuad(arr, visited, x, y + size//2, size//2)
                    zipQuad(arr, visited,  x + size//2, y + size//2, size//2)
                    return  # 안에서 재귀호출뒤 return 하는것 까먹지 말기... 안넣어주면 무한히 돈다.
        ans[color] += 1


ans = [0, 0]


def solution(arr):
    visited = [[False]*len(arr) for _ in range(len(arr))]
    zipQuad(arr, visited, 0, 0, len(arr))
    return ans
